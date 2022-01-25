import sys
sys.path.insert(1, './blockchain explorer/')

from utils import *
from bitcoin import *
from blockchain import *
from wallet import *

#Generate random wallet
wallet = Wallet()
#print(wallet.get_info(address_uncompressed=False,address_compressed=False, public_key=False, balance=True))

#Generate wallet from private key
wallet = Wallet("414136d08c5ed2bf3ba048afe6dcaebafeffffffffffffffffffffffffffffff")
#print(wallet.get_info())

#Generate brain wallet
print("")
print(bip39("aware report multiply exile buyer drum poverty supreme gym oppose float"))

print(hexToBytes("414136d08c5ed2bf3ba048afe6dcaebafeffffffffffffffffffffffffffffff"))
print(bytesToHex([65, 65, 54, 208, 140, 94, 210, 191, 59, 160, 72, 175, 230, 220, 174, 186, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]))