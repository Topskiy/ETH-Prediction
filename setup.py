""" Create Ocean instance and Alice's wallet"""
import os
from dotenv import load_dotenv

from ocean_lib.web3_internal.wallet import Wallet
from ocean_lib.example_config import ExampleConfig
from ocean_lib.ocean.ocean import Ocean

load_dotenv()

config = ExampleConfig.get_config("https://polygon-rpc.com") # points to Polygon mainnet
config["BLOCK_CONFIRMATIONS"] = 10

ocean = Ocean(config)

alice_private_key = os.getenv('REMOTE_TEST_PRIVATE_KEY1')
alice_wallet = Wallet(ocean.web3, alice_private_key,
                config["BLOCK_CONFIRMATIONS"], config["TRANSACTION_TIMEOUT"])
assert alice_wallet.web3.eth.get_balance(alice_wallet.address) > 0, "Alice needs MATIC"
