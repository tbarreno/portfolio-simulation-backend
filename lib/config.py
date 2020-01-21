#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# A pretty basic configuracion module.
#

import os

#
# Data structure configuration ..............................................
#

# Data directory: it may come from a environment variable in a Docker image
if os.getenv("DATA_DIR"):
    data_directory = os.getenv("DATA_DIR")
else:
    data_directory = "data"

# CSV file with the datasets description
dataset_info_file = "datasets.csv"

# CSV file with the dataset content
dataset_constituents = "constituents.csv"

# Symbol data directory
symbols_directory = "symbols"

#
# Listener configuration ....................................................
#

if os.getenv("LISTEN_HOST"):
    listen_host = os.getenv("LISTEN_HOST")
else:
    listen_host = "127.0.0.1"

if os.getenv("LISTEN_PORT"):
    listen_port = os.getenv("LISTEN_PORT")
else:
    listen_port = "5000"

if os.getenv("DEBUG"):
    if os.getenv("DEBUG").lower() == "true":
        listen_debug = True
    else:
        listen_debug = False
else:
    listen_debug = False
