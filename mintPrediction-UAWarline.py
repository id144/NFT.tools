#Contract
#https://etherscan.io/token/0xd3228e099e6596988ae0b73eaa62591c875e5693

#Collection
#https://opensea.io/collection/metahistorymuseum

#Website
#https://metahistory.gallery/
import json
import os
from web3 import Web3
import time
import requests

def getTokenNFT(_token):
    reqSess = requests.Session()  
    
    _url = 'https://ipfs.io/ipfs/QmU3gHF45sRXbyxojhWEJV1m6t5QFk7DuCi4LeSPK87QJ6/' + str(_token)
    try:
        r = reqSess.get(url=_url,timeout=10) 
        usr = r.json()
        return usr['item_number']
    except Exception as e:
        return 0

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/48afa1aa8f2d40f6b701a6491709078a'))

#create contract object
warlineAddress = Web3.toChecksumAddress('0xd3228e099e6596988ae0b73eaa62591c875e5693')
with open("warlineABI.json", "r") as read_file:
    warlineABI = json.load(read_file)
warlineTokenContract = w3.eth.contract(address=warlineAddress, abi=warlineABI)   

def printGasInfo():
    print("Gas price in wei:" + str(w3.fromWei(int(w3.eth.gasPrice*1), 'gwei')))

_oldID = -1
while (True):
    time.sleep(1)
    _currentID = warlineTokenContract.functions.totalSupply().call()
    if _currentID != _oldID:
        _nftID = int(getTokenNFT(_currentID))
        if _nftID != 0:
            _oldID = _currentID

        print("Next to be minted: " + str(_nftID +1) + " ")
        print("Image URL: " +"https://ipfs.io/ipfs/QmWYTbSse2cUNQo1FBpeAS9S7scU8H5655MYSuwFuT5wUE/" +str(_nftID +1) + ".jpg")
        printGasInfo()
