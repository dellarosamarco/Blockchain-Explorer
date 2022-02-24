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

            while(totalAddresses > 0) :
                addresses = []
                if(totalAddresses >= 50) :
                    for n in range(0,50) :
                        addresses.append(self.pool[n].address_compressed)
                        addresses.append(self.pool[n].address_uncompressed)

                    newBalance = get_balances(addresses)
                    if(newBalance > 0) :
                        print(self.getPoolInfo())
                    else :
                        if(totalAddresses >= 100) : 
                            print(str(len(addresses)/2) + " Wallets scanned => 0 BTC")
                        else :
                            print(str(totalAddresses/2) + " Wallets scanned => 0 BTC") 
                    self.poolBalance += newBalance
                    totalAddresses -= 100
                    time.sleep(self.apiTimeLimit)
                else :
                    for n in range(0,len(self.pool)) :
                        addresses.append(self.pool[n].address_compressed)
                        addresses.append(self.pool[n].address_uncompressed)

                    newBalance = get_balances(addresses)
                    if(newBalance > 0) :
                        print(self.getPoolInfo())
                    else :
                        print(str(len(addresses)) + " Wallets scanned => 0 BTC")
                    self.poolBalance += newBalance
                    totalAddresses = 0

            if(self.poolBalance > 0) :
                print(self.getPoolInfo())
            
            return self.poolBalance
        else :
            return self.poolBalance

    def getPoolInfo(self) :
        infos = []

        for n in range(0,len(self.pool)) :
            infos.append(self.pool[n].get_info(balance=False,transactions=False))

        return infos
            