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

#### Generate a 12 words wallet
```python
import test
words = "aware report multiply exile buyer drum poverty supreme gym oppose float aware"
private_key = bip39(words)
wallet = Wallet(private_key)
```

#### Get next and previous private key
```python
import test
#Create a wallet
first_private_key = "0000000000000000000000000000000000000000000000000000000000000001"
first_wallet = Wallet(first_private_key)

#Get the next private key of the wallet
next_private_key = nextPrivateKey(first_wallet.private_key)
print(next_private_key) #0000000000000000000000000000000000000000000000000000000000000002

#Go back to the previous private key
previous_wallet = Wallet(next_private_key)
previous_private_key = previousPrivateKey(previous_wallet.private_key)
previous_wallet = Wallet(previous_private_key)
print(next_wallet.private_key) #0000000000000000000000000000000000000000000000000000000000000001
```
