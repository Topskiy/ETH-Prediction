# ETH Price: Round Three

[The Challenge Readme](https://github.com/oceanprotocol/predict-eth/blob/main/challenges/main4.md)

[The Challenge on Desights](https://desights.ai/challenge/4)

Datatoken: 0x96B72c17DbEDd6905326fccbEA48a931cE99581D

[Arweave prediction saved](https://arweave.net/na9u74yh5gHXEeEwKW9FP7zFHvYdXIjqKPfAXsfhlLc)

## Input data

We downloaded ETH/USDT hourly prices data for the last 1000 observations years from  ocean.

## Processing and Prediction

We further ran data through neural prophet to obtain time series predictions. Check `get-predictions.ipynb`.
Next, we uploaded data to bundlr with `upload.py`. Uploaded data to ocean with `upload_to_ocean.py`. And sent the data to judges via `send_to_judges.py`.
