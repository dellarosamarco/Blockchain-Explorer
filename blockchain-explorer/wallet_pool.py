from blockchainexplorer import *
from wallet import *

class WalletPool :

    pool = []
    
    def __init__(self, poolSize) : 
        self.poolSize = poolSize
        
        for n in range(0,self.poolSize) : 
            self.pool.append(Wallet())
            