# Blockchain Explorer
This is a python library for the Bitcoin blockchain

Installation :

```bash
pip install test
```

Usage :
#### Generate a wallet
```python
import test

#Generate a wallet from a private key
wallet = Wallet("414136d08c5ed2bf3ba048afe6dcaebafeffffffffffffffffffffffffffffff")
balance = wallet.get_balance()
print(balance)


#Generate a random wallet
wallet = Wallet()
balance = wallet.get_balance()
print(balance)


#Generate a wallet from a seed phrase
seed_phrase = "aware report multiply exile buyer drum poverty supreme gym oppose float acid"
private_key = bip39(seed_phrase)
wallet = Wallet(private_key)


#Generate a wallet from a random seed phrase
seed_phrase = random_seed_phrase()
private_key = bip39(seed_phrase)
wallet = Wallet(private_key)
```

#### Get next and previous private key
```python
import test

#Starting private key
private_key_1 = "0000000000000000000000000000000000000000000000000000000000000001"

#Go to the next one
private_key_2 = nextPrivateKey(private_key_1)
print(private_key_2) #0000000000000000000000000000000000000000000000000000000000000002

#Go back to the previous one
private_key_1 = previousPrivateKey(private_key_2)
print(private_key_1) #0000000000000000000000000000000000000000000000000000000000000001
```

Wallet functionalities : 
* Wallet() -> create random wallet
* Wallet(private_key) -> create wallet from a private key
* wallet.get_balance() -> balance
* wallet.private_key -> private key
* wallet.public_key -> public key
* wallet.address_compressed -> address (Compressed)
* wallet.address_uncompressed -> address (Uncompressed)
* wallet.get_info() -> get all the wallet info (private key, public key, addresses, balance)
* wallet.get_info(private_key=False, balance=False) -> get all the wallet info except private key and balance #list of default args => (private_key = True, public_key = True, address_compressed = True, address_uncompressed = True, balance = True)
* wallet.next_wallet() -> next wallet
* wallet.previous_wallet() -> previous wallet

Functions :
* get_balance(address) -> balance
* random_private_key() -> private key
* privkey_to_pubkey(private_key) -> public key
* pubkey_to_addr(public_key,True) -> address (Compressed)
* pubkey_to_addr(public_key,False) -> address (Uncompressed)
* privkey_to_addr(private_key, True) -> address (Compressed)
* privkey_to_addr(private_key, Frue) -> address (Uncompressed)
* bip39(seed_phrase) -> private key
* hexToBytes(hex) -> bytes
* bytesToHex(bytes) -> hex
* nextPrivateKey(private_key) -> private key
* previousPrivateKey(private_key) -> private key
* randomBytes() -> bytes
* random_seed_phrase() -> seed phrase
