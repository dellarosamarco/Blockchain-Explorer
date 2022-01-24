from utils import *
from bitcoin import *
from blockchain import *

class Wallet :
    def __init__(self,private_key = None) :
        if(private_key != None) :
            self.private_key = private_key
        else : 
            self.bytes = randomBytes()
            self.private_key = bytesToHex(self.bytes)
            self.public_key = privkey_to_pubkey(self.private_key)
            self.address_compressed = pubkey_to_addr(self.public_key,True)
            self.address_uncompressed = pubkey_to_addr(self.public_key,True)

        self.info = {}
        self.info["private_key"] = self.private_key
        self.info["public_key"] = self.public_key
        self.info["address_compressed"] = self.address_compressed
        self.info["address_uncompressed"] = self.address_uncompressed

    def get_info(self,private_key = True, public_key = True, address_compressed = True, address_uncompressed = True) :

        response = {}
        
        if(private_key) :
            response["private_key"] = self.private_key
        if(public_key) :
            response["public_key"] = self.public_key
        if(address_compressed) :
           response["address_compressed"] = self.address_compressed
        if(address_uncompressed) :
            response["address_uncompressed"] = self.address_uncompressed
        
        return response
        