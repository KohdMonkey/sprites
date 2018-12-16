import json
import binascii
from pprint import pprint
from web3 import Web3, HTTPProvider 

web3 = Web3(HTTPProvider('http://localhost:8545'))


with open('config.json') as f:
    conf = json.load(f)

pub1 = conf["PUB1"]
pub2 = conf["PUB2"]
priv1 = "0x" + conf["PRIV1"]


contract = web3.eth.contract(
    abi=conf["SPRITES_ABI"],
    bytecode=conf["SPRITES_BYTECODE"])

acct = web3.eth.account.privateKeyToAccount(priv1)
txCount = web3.eth.getTransactionCount(acct.address)


pm_addr = conf["PM_ADDRESS"]


construct_txn = contract.constructor(pm_addr, (pub1, pub2)).buildTransaction({
        'from': acct.address,
        'nonce': web3.eth.getTransactionCount(acct.address),
        'gas': 1728712,
        'gasPrice': web3.toWei('21', 'gwei')})

signed = acct.signTransaction(construct_txn)
web3.eth.sendRawTransaction(signed.rawTransaction)



