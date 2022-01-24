import requests
import json

base_url = "https://blockchain.info/balance?cors=true&active="

def getBalance(compressedAddress = "", uncompressedAddress = "") :
    url = base_url + compressedAddress + "," + uncompressedAddress
    response = requests.get(url)
    response = json.loads(response.text)

    balance = 0
    
    if(compressedAddress != "") :
        balance += response[compressedAddress]["final_balance"]
    elif(uncompressedAddress != "") :
        balance += response[uncompressedAddress]["final_balance"]

    return balance
    

def getBalances(compressedAddresses = [], uncompressedAddresses = []) : 
    url_compressed = base_url
    url_uncompressed = base_url
    for address in compressedAddresses :
        url_compressed += address + ","

    for address in uncompressedAddresses :
        url_uncompressed += address + ","

    response_compressed = requests.get(url_compressed)
    response_uncompressed = requests.get(url_uncompressed)

    response_compressed = json.loads(response_compressed.text)
    response_uncompressed = json.loads(response_uncompressed.text)

    balances = []

    for n in range(0,len(compressedAddresses)) :
        balances.append(0)
        balances[n] += response_compressed[compressedAddresses[n]]["final_balance"]
        balances[n] += response_uncompressed[uncompressedAddresses[n]]["final_balance"]

    return balances

    