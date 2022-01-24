from utils import *
from bitcoin import *
from blockchain import *
from wallet import *

wallet = Wallet()
print(wallet.get_info(address_uncompressed=False,address_compressed=False, public_key=False, balance=True))



# bytes = [randomBytes()]

# for n in range(0,10) :
#     valueBytes = list(bytes[n])
#     bytes.append(nextBitcoinBytes(valueBytes))

# addresses_c = []
# addresses_u = []
# print(getBalances(addresses_c,addresses_u))