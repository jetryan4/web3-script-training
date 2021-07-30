from web3 import Web3

node_provider = 'https://mainnet.infura.io/v3/144c3c2bb02e48a6ac1dabf4aa882f85'

web3_connection = Web3(Web3.HTTPProvider(node_provider))

def test_connection():
    print(web3_connection.isConnected())

def lastest_block():
    print(web3_connection.eth.block_number)

def balance_of(ETH_address):
    balance = web3_connection.eth.get_balance(ETH_address)
    new_balance = web3_connection.fromWei(balance, 'ether')
    print(new_balance)