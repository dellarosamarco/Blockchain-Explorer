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
```

#### Generate a wallet from a private key
```python
import test
wallet = Wallet("414136d08c5ed2bf3ba048afe6dcaebafeffffffffffffffffffffffffffffff")

print(wallet.private_key)
print(wallet.public_key)
print(wallet.address_compressed)
print(wallet.address_uncompressed)
print(wallet.get_balance())
```
