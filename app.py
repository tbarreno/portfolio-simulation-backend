#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# REST service start script.
#

import flask
from flask_cors import CORS
from flask_restful import Api

import lib.config as config
import resources.info as info
import resources.datasets as dataset
import resources.symbols as symbols
import resources.portfolios as portfolios

# Flask application setup
app = flask.Flask(__name__)
CORS(app)
api = Api(app)

# Resources paths
api.add_resource(info.BackendInformation, '/')
api.add_resource(dataset.DataSets, '/datasets')
api.add_resource(portfolios.Portfolios, '/portfolios')
api.add_resource(dataset.DataSet, '/datasets/<string:shortname>')
api.add_resource(symbols.Symbol, '/symbols/<string:symbol_name>')

if __name__ == '__main__':
    app.run(debug=config.listen_debug,
            host=config.listen_host,
            port=config.listen_port)
