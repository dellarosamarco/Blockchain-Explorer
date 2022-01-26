# Blockchain Explorer
This is a python library for the Bitcoin blockchain

Installation :

```bash
pip install test
```

Usage :
#### Generate a random wallet
```python
import test
wallet = Wallet()

print(wallet.private_key)
print(wallet.public_key)
print(wallet.address_compressed)
print(wallet.address_uncompressed)
print(wallet.get_balance())
print(wallet.get_info())
```

#### Generate a wallet from a private key
```python
import test
wallet = Wallet("414136d08c5ed2bf3ba048afe6dcaebafeffffffffffffffffffffffffffffff")
```

#### Get balance of a wallet 
```python
import test
wallet = Wallet()
print(wallet.get_balance())
```

#### Generate a random seed phrase
```
import test
seed_phrase = random_seed_phrase()
print(seed_phrase)    #aware report multiply exile buyer drum poverty supreme gym oppose float acid
private_key = bip39(seed_phrase)
wallet = Wallet(private_key)
```python

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
