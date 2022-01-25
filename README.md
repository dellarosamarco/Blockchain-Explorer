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
private_key = bip39(worrds)
wallet = Wallet(private_key)
```
