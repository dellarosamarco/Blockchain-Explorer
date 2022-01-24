import requests
import json

base_url = "https://blockchain.info/balance?cors=true&active="

def getBalance(compressedAddress = None, uncompressedAddress = None) :
    url = base_url + compressedAddress + "," + uncompressedAddress
    response = requests.get(url)
    response = json.loads(response.text)
    balance = response[compressedAddress]["final_balance"] + response[uncompressedAddress]["final_balance"]
    return balance
    
    

def getBalances(compressedAddresses = [], uncompressedAddress = []) : 
    pass