""" Upload data"""
import os
from pybundlr import pybundlr
from dotenv import load_dotenv

from ocean_lib.ocean.ocean import Ocean
from ocean_lib.web3_internal.wallet import Wallet
from ocean_lib.example_config import ExampleConfig

load_dotenv()

FILE_NAME = './eth_predict.csv'

alice_private_key = os.getenv('REMOTE_TEST_PRIVATE_KEY1')

config = ExampleConfig.get_config("https://polygon-rpc.com") # points to Polygon mainnet
config["BLOCK_CONFIRMATIONS"] = 5
ocean = Ocean(config)

alice_wallet = Wallet(ocean.web3, alice_private_key,
                      config["BLOCK_CONFIRMATIONS"], config["TRANSACTION_TIMEOUT"])

assert alice_wallet.web3.eth.get_balance(alice_wallet.address) > 0, "Alice needs MATIC"

url = pybundlr.fund_and_upload(FILE_NAME, "matic", alice_wallet.private_key)
print(f"Your csv url: {url}")
