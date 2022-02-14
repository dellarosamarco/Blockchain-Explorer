from blockchainexplorer import *
from wallet import *
import time

class WalletPool :
    pool = []
    poolBalance = None
    apiTimeLimit = 2
    
    def __init__(self, poolSize) : 
        self.poolSize = poolSize
        
        for n in range(0,self.poolSize) : 
            self.pool.append(Wallet())

    def getPoolBalance(self) :
        if(self.poolBalance == None) :
            self.poolBalance = 0
            addresses = []
            totalAddresses = len(self.pool) * 2
            poolLength = len(self.pool)

            while(totalAddresses != 0) :
                addresses = []
                if(poolLength >= 50) :
                    for n in range(0,50) :
                        addresses.append(self.pool[n].address_compressed)
                        addresses.append(self.pool[n].address_uncompressed)
        
                    self.poolBalance += get_balances(addresses)
                    totalAddresses -= 100
                    time.sleep(self.apiTimeLimit)
                else :
                    for n in range(0,len(self.pool)) :
                        addresses.append(self.pool[n].address_compressed)
                        addresses.append(self.pool[n].address_uncompressed)
        
                    self.poolBalance += get_balances(addresses)
                    totalAddresses = 0

            if(self.poolBalance > 0) :
                print(self.getPoolInfo())
            
            return "Pool balance : " + str(self.poolBalance) + " BTC"
        else :
            return "Pool balance : " + str(self.poolBalance) + " BTC"

    def getPoolInfo(self) :
        infos = []

        for n in range(0,len(self.pool)) :
            infos.append(self.pool[n].get_info(balance=False))

        return infos
            