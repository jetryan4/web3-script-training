import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
node_provider = os.environ['NODE_PROVIDER_LOCAL']
web3_connection = Web3(Web3.HTTPProvider(node_provider))

global_gas = 4500000
global_gas_price = web3_connection.toWei(8, 'gwei') # gwei and wei are fractions of eth price

def test_connection():
    return web3_connection.isConnected()

def get_nonce(ETH_address):
    return web3_connection.eth.get_transaction_count(ETH_address)

def transfer_ETH(sender, receiver, signature, amount_ETH):
    transaction_body = {
        'nonce': get_nonce(sender),
        'to':receiver,
        'value':web3_connection.toWei(amount_ETH, 'ether'),
        'gas': global_gas,
        'gasPrice': global_gas_price
    }
    signed_transaction = web3_connection.eth.account.sign_transaction(transaction_body, signature)
    result = web3_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return result
