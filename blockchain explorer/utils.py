import random
import codecs

def bytesToHex(bytesArray) :
    return ''.join('{:02x}'.format(byte) for byte in bytesArray)

def hexToBytes(hex) :
    return [int(hex[i:i+2],16) for i in range(0,len(hex),2)]

def nextBitcoinBytes(bytesArray) :
    index = 31
    bytesArray[index] += 1

    while(bytesArray[index] > 255) :
        bytesArray[index] = 0
        index-=1
        bytesArray[index] += 1

    return bytesArray

def randomBytes() :
    bytesArray = []
    for n in range(0,32) :
        bytesArray.append(random.randint(0,255))
    return bytesArray