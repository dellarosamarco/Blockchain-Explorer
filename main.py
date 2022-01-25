import sys
sys.path.insert(1, './blockchain explorer/')

from bitcoin import *
from wallet import *

#Generate random wallet
wallet = Wallet()
#print(wallet.get_info(address_uncompressed=False,address_compressed=False, public_key=False, balance=True))

#Generate wallet from private key
wallet = Wallet("414136d08c5ed2bf3ba048afe6dcaebafeffffffffffffffffffffffffffffff")
#print(wallet.get_info())

#Generate brain wallet
print("")
private_key = bip39("aware report multiply exile buyer drum poverty supreme gym oppose float aware")
wallet_2 = Wallet(private_key)
#print(wallet_2.get_info(balance=True))

#Get balance of a wallet
wallet = Wallet("414136d08c5ed2bf3ba048afe6dcaebafeffffffffffffffffffffffffffffff")
#print(wallet.get_balance())

#Get balance of an address
address = "1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH"
#print(get_balance(address))

#Get next wallet
wallet = Wallet("0000000000000000000000000000000000000000000000000000000000000001")
#print(wallet.private_key)
next_private_key = nextPrivateKey(wallet.private_key)
next_wallet = Wallet(next_private_key)
#print(next_wallet.private_key)

#Get previous wallet
wallet = Wallet("0000000000000000000000000000000000000000000000000000000000000002")
#print(wallet.private_key)
next_private_key = previousPrivateKey(wallet.private_key)
next_wallet = Wallet(next_private_key)
#print(next_wallet.private_key)

#Get address from private key
private_key = "0000000000000000000000000000000000000000000000000000000000000001"
#print(privkey_to_addr(private_key, compressed=True))
#print(privkey_to_addr(private_key, compressed=False))


#Generate random seed phrase
print(random_seed_phrase())