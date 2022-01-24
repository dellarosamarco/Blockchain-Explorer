from utils import *
from bitcoin import *

bytes = [randomBytes()]

for n in range(0,10) :
    valueBytes = list(bytes[n])
    bytes.append(nextBitcoinBytes(valueBytes))

for byte in bytes :
    private_key = bytesToHex(byte)
    public_key = privkey_to_pubkey(private_key)
    address_compressed = pubkey_to_addr(public_key,True)
    address_uncompressed = pubkey_to_addr(public_key,False)

    print("Private key : " + private_key)
    print("Address (Compressed) : " + address_compressed)
    print("Address (Uncompressed) : " + address_uncompressed)


#print(bytesToHex(bytes))