"""Upload prediction to OCEAN"""
import os
from ocean_lib.web3_internal.wallet import Wallet
from ocean_lib.example_config import ExampleConfig
from ocean_lib.ocean.ocean import Ocean
from dotenv import load_dotenv

load_dotenv()

URL = "https://arweave.net/WFpfNY0gXVxkTCT9aBTqgVlVWlY0WwpcA17G8sGlVSY"
NAME = "ETH predictions 3"

config = ExampleConfig.get_config("https://polygon-rpc.com") # points to Polygon mainnet
config["BLOCK_CONFIRMATIONS"] = 4 #faster
ocean = Ocean(config)

alice_private_key = os.getenv('REMOTE_TEST_PRIVATE_KEY1')
alice_wallet = Wallet(ocean.web3, alice_private_key,
                       config["BLOCK_CONFIRMATIONS"], config["TRANSACTION_TIMEOUT"])
assert alice_wallet.web3.eth.get_balance(alice_wallet.address) > 0, "Alice needs MATIC"

# Publish the csv as an Ocean asset, in Polygon
asset = ocean.assets.create_url_asset(NAME, URL, alice_wallet)
