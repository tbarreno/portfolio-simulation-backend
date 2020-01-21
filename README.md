
# Portfolio Simulation Backend

Just a simple **Python** backend for a stock portfolio practice application.

It's a Flask based REST services with filesystem storage at this moment.

*This project is still in heavy development state.*

## API

The current endpoints of the service:

- `GET /info`: Returns a static object with the backend version.
- `GET /datasets`: Returns the list of available datasets
- `GET /datasets/<id>`: Returns the list of stock symbols for a given dataset.
- `POST /portfolio`: Sends a portfolio (a list of pairs
  'symbol-name, quantity') to the server to run the simulation.

## Installation

Just install a **Python 3.7** virtual environment with the packages included
in the `requirements.txt` file.

```sh
pip install -r requirements.txt
```

The Docker container can be build with:

```sh
docker image build -t portfolio_simulator_bk:1.0 .
```
