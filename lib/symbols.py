#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# A module for accessing symbol information.
#

import pandas as pd
import os.path
from lib import config, exceptions


def get_symbol_data(symbol_name):
    """Returns the symbol data as a Pandas DataFrame."""

    # Symbol data file
    symbol_filename = f"{symbol_name}_data.csv"
    symbol_file = os.path.join(config.data_directory,
                               config.symbols_directory,
                               symbol_filename)

    # Check for the file
    if not os.path.exists(symbol_file):
        raise exceptions.ResourceNotFoundException(
            f"The symbol '{symbol_name}' was not available.")

    # Open the data
    symbol_data = pd.read_csv(symbol_file, index_col=0)

    return symbol_data


def get_symbol_historical(symbol_name):
    """Returns the available historical data for a symbol as a dictionary."""

    # Get the data
    symbol_data = get_symbol_data(symbol_name)

    # Build the response
    response = symbol_data.to_dict(orient="records")

    return response


def exists(symbol_name):
    """Check the symbol availability. Returns true/false."""

    symbol_filename = f"{symbol_name}_data.csv"
    symbol_file = os.path.join(config.data_directory,
                               config.symbols_directory,
                               symbol_filename)

    # Check for the file
    return os.path.exists(symbol_file)
