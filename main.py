import sys
sys.path.insert(1, './blockchain explorer/')

from utils import *
from bitcoin import *
from blockchain import *
from wallet import *

#Generate random wallet
wallet = Wallet()
print(wallet.get_info(address_uncompressed=False,address_compressed=False, public_key=False, balance=True))

#Generate wallet from private key
wallet = Wallet("414136d08c5ed2bf3ba048afe6dcaebafeffffffffffffffffffffffffffffff")
print(wallet.get_info())