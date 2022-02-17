import sys
sys.path.append("blockchain-explorer/")
from blockchainexplorer import *
from wallet import *
from wallet_pool import *



wallet = Wallet()
tx = wallet.get_transactions()
print(tx)