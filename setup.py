""" Create Ocean instance and Alice's wallet"""
import os
from dotenv import load_dotenv

from ocean_lib.ocean.ocean import Ocean
from ocean_lib.web3_internal.utils import connect_to_network
from ocean_lib.example_config import get_config_dict

load_dotenv()

def create_ocean_instance(network_name: str) -> Ocean:
    config = get_config_dict(network_name)
    config["BLOCK_CONFIRMATIONS"] = 1  # faster
    connect_to_network(network_name)
    ocean = Ocean(config)
    return ocean

def load_from_ohlc_data(file_name: str) -> tuple:
    """Returns (list_of_unixtimes, list_of_close_prices)"""
    with open(file_name, "r") as file:
        data_str = file.read().rstrip().replace('"', "")
    x = eval(data_str)  # list of lists
    uts = [xi[0] / 1000 for xi in x]
    vals = [xi[4] for xi in x]
    return (uts, vals)

def create_alice_wallet(ocean: Ocean) -> LocalAccount:
    config = ocean.config_dict
    alice_private_key = os.getenv("REMOTE_TEST_PRIVATE_KEY1")
    alice_wallet = accounts.add(alice_private_key)
    bal = Web3.fromWei(accounts.at(alice_wallet.address).balance(), "ether")
    print(f"alice_wallet.address={alice_wallet.address}. bal={bal}")
    assert bal > 0, f"Alice needs MATIC"
    return alice_wallet

ocean = create_ocean_instance("matic")
alice_wallet = create_alice_wallet(ocean) #you're Alice

ETH_USDT_did = "did:op:0dac5eb4965fb2b485181671adbf3a23b0133abf71d2775eda8043e8efc92d19"
file_name = ocean.assets.download_file(ETH_USDT_did, alice_wallet)
allcex_uts, allcex_vals = load_from_ohlc_data(file_name)
#print_datetime_info("CEX data info", allcex_uts)
