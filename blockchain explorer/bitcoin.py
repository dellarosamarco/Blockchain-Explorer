import hashlib
import base58
import codecs
import ecdsa

import pprint
import binascii
import mnemonic
import bip32utils

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