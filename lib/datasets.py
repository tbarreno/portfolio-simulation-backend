#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# A module for getting the avilable datasets and stocks infomation.
#

import pandas as pd
import os.path
from lib import config, exceptions

# Dataset description file
dataset_file = os.path.join(config.data_directory, config.dataset_info_file)


def get_all_datasets():
    """Load the data files and returns a list of datasets."""

    # Open the 'datasets.csv' file and get the information
    datasets = pd.read_csv(dataset_file)

    # Build the response
    response = []

    for index, row in datasets.iterrows():
        # Build the response object (returns the dataset
        # short and long names and availability dates).
        response.append({
            "shortname": row["shortname"],
            "name": row["name"]
        })

    return response


def get_dataset_detail(shortname):
    """Returns the dataset detail and available stocks"""

    # Open the 'datasets.csv' file
    datasets = pd.read_csv(dataset_file)

    print(f"[get_dataset_detail] shortname = '{shortname}'")

    # Get the directory for this dataset
    data_entry = datasets.loc[datasets["shortname"] == shortname]["directory"]

    # Verify that the dataset exists
    if data_entry.empty:
        raise exceptions.ResourceNotFoundException(
            f"The dataset '{shortname}' was not found on the backend.")

    # Get the data directory
    data_dir = data_entry.iloc[0]

    # Build the full path to the constituents file
    constituents_file = os.path.join(config.data_directory, data_dir, config.dataset_constituents)

    # Read the stock listing file (constituents) converting each one to a
    # dictionary
    constituents_data = pd.read_csv(constituents_file)

    response = constituents_data.to_dict(orient="records")

    return response
