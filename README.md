# ETH Price: Round Three

[The Challenge Readme](https://github.com/oceanprotocol/predict-eth/blob/main/challenges/main3.md)

[The Challenge on Desights](https://desights.ai/g/challenge/1)

`INFO:ocean:Successfully created NFT with address 0x17e4a572D9cA398f66070Fed842FF819f5B689b0.
INFO:ocean:Successfully created datatoken with address 0x222F74ad94C3d9C1673bb43FE611c8E456082b7C.`

[Arweave prediction saved](https://arweave.net/WFpfNY0gXVxkTCT9aBTqgVlVWlY0WwpcA17G8sGlVSY)

## Input data

We downloaded ETH/USDT hourly prices data for the last 2 years from binance using `download_data.py`.

## Processing and Prediction

We further ran data through prophet to obtain time series predictions. Check `get-predictions.ipynb` and also [Kaggle Notebook](https://www.kaggle.com/pavfedotov/predict-eth-price).

Next, we uploaded data to bundlr with `upload.py`. Uploaded data to ocean with `upload_to_ocean.py`. And sent the data to judges via `send_to_judges.py`.

## Further Research

We started the LSTM notebook, but did not have enough time to validate and optimize hyperparameters.

[LSTM Notebook](https://www.kaggle.com/code/pavfedotov/ethereum-price-prediction)
