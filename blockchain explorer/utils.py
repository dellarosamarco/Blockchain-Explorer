import random
import codecs

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