from blockchainexplorer import *
from wallet import *
from wallet_pool import *

walletsToGenerate = 125

walletPool = WalletPool(walletsToGenerate)
print(walletPool.getPoolBalance())