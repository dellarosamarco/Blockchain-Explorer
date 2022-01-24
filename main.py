from utils import *
from bitcoin import *
from blockchain import *

bytes = [randomBytes()]

for n in range(0,10) :
    valueBytes = list(bytes[n])
    bytes.append(nextBitcoinBytes(valueBytes))

addresses_c = []
addresses_u = []

for byte in bytes :
    private_key = bytesToHex(byte)
    public_key = privkey_to_pubkey(private_key)
    address_compressed = pubkey_to_addr(public_key,True)
    address_uncompressed = pubkey_to_addr(public_key,False)
    addresses_c.append(address_compressed)
    addresses_u.append(address_uncompressed)

    print("Private key : " + private_key)
    # print("Address (Compressed) : " + address_compressed)
    # print("Address (Uncompressed) : " + address_uncompressed)
    # print("Balance : " + str(getBalance(address_compressed, address_uncompressed)))

print(getBalances(addresses_c,addresses_u))






#print(bytesToHex(bytes))