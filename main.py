from utils import *

bytes = [randomBytes()]

for n in range(0,10) :
    valueBytes = list(bytes[n])
    bytes.append(nextBitcoinBytes(valueBytes))

for byte in bytes :
    print(bytesToHex(byte))

#print(bytesToHex(bytes))