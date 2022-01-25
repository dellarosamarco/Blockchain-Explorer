import hashlib
import base58
import codecs
import ecdsa
import binascii
import mnemonic
import bip32utils
import requests
import json
import random

base_url = "https://blockchain.info/balance?cors=true&active="

def privkey_to_pubkey(private_key) :
    private_key_bytes = codecs.decode(private_key, 'hex')
    public_key_raw = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
    public_key_bytes = public_key_raw.to_string()
    public_key_hex = codecs.encode(public_key_bytes, 'hex')
    public_key = (b'04' + public_key_hex).decode("utf-8")
    return public_key

def pubkey_to_addr(public_key, compressed) : 
    if(compressed) :  
        if (ord(bytearray.fromhex(public_key[-2:])) % 2 == 0):
            public_key_compressed = '02'
        else:
            public_key_compressed = '03'
            
        public_key_compressed += public_key[2:66]
    
        hex_str = bytearray.fromhex(public_key_compressed)
    else : 
        hex_str = bytearray.fromhex(public_key)
        
    sha = hashlib.sha256()
    sha.update(hex_str)

    rip = hashlib.new('ripemd160')
    rip.update(sha.digest())
    key_hash = rip.hexdigest()

    modified_key_hash = "00" + key_hash

    sha = hashlib.sha256()
    hex_str = bytearray.fromhex(modified_key_hash)
    sha.update(hex_str)

    sha_2 = hashlib.sha256()
    sha_2.update(sha.digest())

    checksum = sha_2.hexdigest()[:8]

    byte_25_address = modified_key_hash + checksum

    address = base58.b58encode(bytes(bytearray.fromhex(byte_25_address))).decode('utf-8')

    return address

def privkey_to_addr(private_key,compressed) :
    public_key = privkey_to_pubkey(private_key)
    address = pubkey_to_addr(public_key, compressed)
    return address


def bip39(mnemonic_words):
    mobj = mnemonic.Mnemonic("english")
    seed = mobj.to_seed(mnemonic_words)

    bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
    bip32_child_key_obj = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(0)

    wif = bip32_child_key_obj.WalletImportFormat()
    private_key = wif_to_privkey(wif)

    return private_key

def wif_to_privkey(wif):    
    first_encode = base58.b58decode(wif)
    private_key_full = binascii.hexlify(first_encode)
    private_key = private_key_full[2:-10]
    return private_key.decode("utf-8")
    
def get_balance(compressedAddress = "", uncompressedAddress = "") :
    url = base_url + compressedAddress + "," + uncompressedAddress
    response = requests.get(url)
    response = json.loads(response.text)

    balance = 0
    
    if(compressedAddress != "") :
        balance += response[compressedAddress]["final_balance"]
    elif(uncompressedAddress != "") :
        balance += response[uncompressedAddress]["final_balance"]

    return balance
    

def get_balances(compressedAddresses = [], uncompressedAddresses = []) : 
    url_compressed = base_url
    url_uncompressed = base_url
    for address in compressedAddresses :
        url_compressed += address + ","

    for address in uncompressedAddresses :
        url_uncompressed += address + ","

    response_compressed = requests.get(url_compressed)
    response_uncompressed = requests.get(url_uncompressed)

    response_compressed = json.loads(response_compressed.text)
    response_uncompressed = json.loads(response_uncompressed.text)

    balances = []

    for n in range(0,len(compressedAddresses)) :
        balances.append(0)
        balances[n] += response_compressed[compressedAddresses[n]]["final_balance"]
        balances[n] += response_uncompressed[uncompressedAddresses[n]]["final_balance"]

    return balances

def bytesToHex(bytesArray) :
    return ''.join('{:02x}'.format(byte) for byte in bytesArray)

def hexToBytes(hex) :
    return [int(hex[i:i+2],16) for i in range(0,len(hex),2)]

def nextPrivateKey(private_key) :
    bytesArray = hexToBytes(private_key)
    index = 31
    bytesArray[index] += 1

    while(bytesArray[index] > 255) :
        bytesArray[index] = 0
        index-=1
        bytesArray[index] += 1

    private_key = bytesToHex(bytesArray)
    return private_key

def previousPrivateKey(private_key) :
    bytesArray = hexToBytes(private_key)
    index = 31
    bytesArray[index] -= 1

    while(bytesArray[index] < 0) :
        bytesArray[index] = 255
        index-=1
        bytesArray[index] -= 1

    for byte in bytesArray : 
        if(byte > 255 or byte < 0) :
            return ValueError("Invalid private key")

    valid = False

    for byte in bytesArray :
        if(byte != 0) :
            valid = True
            break

    if(valid == False) :
        raise ValueError("Invalid private key")
    

    private_key = bytesToHex(bytesArray)
    return private_key

def randomBytes() :
    bytesArray = []
    for n in range(0,32) :
        bytesArray.append(random.randint(0,255))
    return bytesArray

def random_seed_phrase() :
    file = open("./blockchain explorer/english.txt","r")
    seed = []
    words = []
    for word in file.readlines() :
        words.append(word.rstrip("\n"))

    for n in range(0,12) :
        seed.append(words[random.randint(0,len(words))])
    return seed