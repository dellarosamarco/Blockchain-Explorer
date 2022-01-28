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
next_private_key = next_private_key(wallet.private_key)
next_wallet = Wallet(next_private_key)
#print(next_wallet.private_key)

#Get previous wallet
wallet = Wallet("0000000000000000000000000000000000000000000000000000000000000002")
#print(wallet.private_key)
next_private_key = previous_private_key(wallet.private_key)
next_wallet = Wallet(next_private_key)
#print(next_wallet.private_key)

#Get address from private key
private_key = "0000000000000000000000000000000000000000000000000000000000000001"
#print(privkey_to_addr(private_key, compressed=True))
#print(privkey_to_addr(private_key, compressed=False))


#Generate random seed phrase
#print(random_seed_phrase())


#Generate random private key
#print(random_private_key())

#Get next and previosu wallet
wallet = Wallet("0000000000000000000000000000000000000000000000000000000000000002")
next_wallet = wallet.next_wallet()
#print(next_wallet.private_key)

previous_wallet = wallet.previous_wallet()
#print(previous_wallet.private_key)


#print(privkey_to_pubkey("37a5dc73e1162be2d5484b8507723f32fb676717702e99492d7983b79d03ac5e"))

#print(pubkey_to_addr("040498e8bf7f4de756bb8d5df7632f843e49a4268c61d1dd704c2858a63cb9da1379e94b148e845da87ce3112144449d3cddbe9861a298eeaf375c2ae1134ab87e",True))

#print(pubkey_to_addr("040498e8bf7f4de756bb8d5df7632f843e49a4268c61d1dd704c2858a63cb9da1379e94b148e845da87ce3112144449d3cddbe9861a298eeaf375c2ae1134ab87e",False))

#print(bip39("aware report multiply exile buyer drum poverty supreme gym oppose float acid"))

#print(hex_to_bytes("fd355dcd6ee9dc740c00d332de4213d3b30cc52f6f64f050e03af437401eec7f"))

#print(random_bytes())

print(random_seed_phrase())
