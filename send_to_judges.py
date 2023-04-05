"""Share predictions to judges, in Polygon"""
import os
from ocean_lib.web3_internal.wallet import Wallet
from ocean_lib.example_config import ExampleConfig
from ocean_lib.ocean.ocean import Ocean
from ocean_lib.models.datatoken import Datatoken
from dotenv import load_dotenv

load_dotenv()

config = ExampleConfig.get_config("https://polygon-rpc.com") # points to Polygon mainnet
config["BLOCK_CONFIRMATIONS"] = 4 #faster
ocean = Ocean(config)

alice_private_key = os.getenv('REMOTE_TEST_PRIVATE_KEY1')

alice_wallet = Wallet(ocean.web3, alice_private_key,
                       config["BLOCK_CONFIRMATIONS"], config["TRANSACTION_TIMEOUT"])

datatoken = Datatoken(ocean.web3, "0x96B72c17DbEDd6905326fccbEA48a931cE99581D")

datatoken.mint("0xA54ABd42b11B7C97538CAD7C6A2820419ddF703E", ocean.to_wei(10), alice_wallet)
