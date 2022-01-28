# Blockchain Explorer
This is a python library for the Bitcoin blockchain

### Installation :

```bash
pip install test
```

### Usage :
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


#Get the next and previous wallet
wallet = Wallet("0000000000000000000000000000000000000000000000000000000000000002")

next_wallet = wallet.next_wallet()
print(next_wallet.private_key) #0000000000000000000000000000000000000000000000000000000000000003

previous_wallet = wallet.previous_wallet()
print(previous_wallet.private_key) #0000000000000000000000000000000000000000000000000000000000000001
```


Wallet functionalities list : 
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


#### Useful functions usage
```python
import test

#Get balance of an address
address = "34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo"
balance = get_balance(address)
print(balance) #265479 BTC

#Generate a random private key
private_key = random_private_key()
print(private_key) #37a5dc73e1162be2d5484b8507723f32fb676717702e99492d7983b79d03ac5e

#Convert private key to public key
private_key = "37a5dc73e1162be2d5484b8507723f32fb676717702e99492d7983b79d03ac5e"
public_key = privkey_to_pubkey(private_key)
print(public_key) #040498e8bf7f4de756bb8d5df7632f843e49a4268c61d1dd704c2858a63cb9da1379e94b148e845da87ce3112144449d3cddbe9861a298eeaf375c2ae1134ab87e

#Convert public key to address (Compressed/Uncompressed)
public_key = "040498e8bf7f4de756bb8d5df7632f843e49a4268c61d1dd704c2858a63cb9da1379e94b148e845da87ce3112144449d3cddbe9861a298eeaf375c2ae1134ab87e"
address_compressed = pubkey_to_addr(public_key,True) #13vrcFSJsKm9MC4c95ZYmnJwLmHXrz1rCV
address_uncompressed = pubkey_to_addr(public_key,False) #1DMJ5zriUX3AH3LLmvhomFzXLfztA8r9xC

#Convert private key to address (Compressed/Uncompressed)
public_key = "37a5dc73e1162be2d5484b8507723f32fb676717702e99492d7983b79d03ac5e"
address_compressed = pubkey_to_addr(public_key,True) #13vrcFSJsKm9MC4c95ZYmnJwLmHXrz1rCV
address_uncompressed = pubkey_to_addr(public_key,False) #1DMJ5zriUX3AH3LLmvhomFzXLfztA8r9xC

#Convert seed phrase to private key
seed_phrase = "aware report multiply exile buyer drum poverty supreme gym oppose float acid"
private_key = bip39(seed_phrase)
print(private_key) #fd355dcd6ee9dc740c00d332de4213d3b30cc52f6f64f050e03af437401eec7f

#Convert private key to bytes
private_key = "fd355dcd6ee9dc740c00d332de4213d3b30cc52f6f64f050e03af437401eec7f"
bytes = hex_to_bytes(private_key)
print(bytes) #[253, 53, 93, 205, 110, 233, 220, 116, 12, 0, 211, 50, 222, 66, 19, 211, 179, 12, 197, 47, 111, 100, 240, 80, 224, 58, 244, 55, 64, 30, 236, 127]

#Convert bytes to private key
bytes = [253, 53, 93, 205, 110, 233, 220, 116, 12, 0, 211, 50, 222, 66, 19, 211, 179, 12, 197, 47, 111, 100, 240, 80, 224, 58, 244, 55, 64, 30, 236, 127]
private_key = bytes_to_hex(bytes)
print(private_key) #fd355dcd6ee9dc740c00d332de4213d3b30cc52f6f64f050e03af437401eec7f

#Get next and previous private key
private_key = "0000000000000000000000000000000000000000000000000000000000000002"

next_private_key = next_private_key(private_key)
print(next_private_key) #0000000000000000000000000000000000000000000000000000000000000003

previous_private_key = previous_private_key(private_key)
print(previous_private_key) #0000000000000000000000000000000000000000000000000000000000000001

#Generate random bytes
bytes = random_bytes()
print(bytes) #[218, 176, 2, 10, 195, 208, 240, 183, 87, 215, 105, 44, 181, 77, 46, 126, 64, 38, 123, 7, 237, 190, 110, 243, 205, 127, 58, 64, 121, 130, 57, 237]

#Generate random seed phrase
seed_phease = random_seed_phrase()
print(seed_phrase) #finger cruel wage scout work theme orphan confirm problem hair resultcycle
```

Useful functions list :
* get_balance(address) -> balance
* random_private_key() -> private key
* privkey_to_pubkey(private_key) -> public key
* pubkey_to_addr(public_key,True) -> address (Compressed)
* pubkey_to_addr(public_key,False) -> address (Uncompressed)
* privkey_to_addr(private_key, True) -> address (Compressed)
* privkey_to_addr(private_key, Frue) -> address (Uncompressed)
* bip39(seed_phrase) -> private key
* hex_to_bytes(hex) -> bytes
* bytes_to_hex(bytes) -> hex
* next_private_key(private_key) -> private key
* previous_private_key(private_key) -> private key
* random_bytes() -> bytes
* random_seed_phrase() -> seed phrase
