#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from flask_restful import Resource, reqparse
from lib import portfolios, symbols, exceptions

parser = reqparse.RequestParser()
parser.add_argument('portfolio', type=dict, action="append", required=True)

class Portfolios(Resource):
    """This resource do the portfolio evaluation on historical prices."""

    def post(self):
        """POST response."""

        # Prepare the response
        response = {}

        try:
            # Check the portfolio content
            sent_data = parser.parse_args()

            # Check that we have the 'portfolio' element
            if sent_data["portfolio"] is None:
                response["status"] = "error"
                response["message"] = "Incorrect portfolio data (missing the 'portfolio' entry)."
                return response, 400

            print(f" > {sent_data}")
            listing = sent_data["portfolio"]

            if type(listing) is not list:
                response["status"] = "error"
                response["message"] = "Incorrect portfolio data (not a list)."
                return response, 400

            # Now loop over the elements for checking the structure
            for entry in listing:

                if 'symbol' not in entry or 'quantity' not in entry:
                    response["status"] = "error"
                    response["message"] = "Incorrect portfolio data (entries must have 'symbol' and 'quantity' values)."
                    return response, 400

            # Do the simulation
            data = portfolios.simulate_portfolio(listing)

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