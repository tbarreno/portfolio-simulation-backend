#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Resource module for dataset information.
#

from flask_restful import Resource
from lib import symbols, exceptions


class Symbol(Resource):
    """This resource returns a 'Symbol' historical data."""

    def get(self, symbol_name):
        """GET response."""

        # Prepare the response
        response = {}

        try:
            # Get the stocks on this dataset
            data = symbols.get_symbol_historical(symbol_name)

            response["status"] = "success"
            response["data"] = data

            return response, 200

        # ...basic error handling
        except exceptions.ResourceNotFoundException as e:
            response["status"] = "error"
            response["message"] = e.message
            return response, 404

        except Exception as e:
            response["status"] = "error"
            if hasattr(e, 'message'):
                response["message"] = e.message
            else:
                response["message"] = "There was some problem while getting the data."
                response["detail"] = f"{e}"
                print(f"ERROR: \n{e}")

            return response, 400