#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Portfolio module.
#

import pandas as pd
from lib import config, exceptions, symbols

def simulate_portfolio(portfolio):
    """Returns the historical value of the full portfolio."""

    sim_data = pd.DataFrame()
    sim_names = []

    for entry in portfolio:

        symbol_name = entry['symbol']
        quantity = int(entry['quantity'])
        sim_names.append(symbol_name)

        print(f" + symbol: {symbol_name}, quantity: {quantity}")

        # Load the symbol data
        symbol_data = symbols.get_symbol_data(symbol_name)

        # Use the 'close' value to simulate the value
        symbol_data[symbol_name] = symbol_data['close'] * quantity

        # Now get the selected columns
        selected_data = symbol_data[["date", symbol_name]]

        # And add it to the response
        if sim_data.shape[0] == 0:
            sim_data = selected_data
        else:
            sim_data = pd.merge(sim_data, selected_data, on="date")

    # Finally, add the portfolio value
    sim_data["portfolio_value"] = sim_data[sim_names].sum(axis=1)

    return sim_data.to_dict(orient="records")
