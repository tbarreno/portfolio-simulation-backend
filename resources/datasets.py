#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Resource module for dataset information.
#

from flask_restful import Resource
from lib import datasets, exceptions


class DataSets(Resource):
    """This resource returns all dataset groups and availability dates."""

    def get(self):
        """GET response."""

        # Prepare the response
        response = {}

        try:
            # Get the dataset information
            data = datasets.get_all_datasets()

            response["status"] = "success"
            response["data"] = data

            return response, 200

        # ...basic error handling
        except Exception as e:
            response["status"] = "error"
            if hasattr(e, 'message'):
                response["message"] = e.message
            else:
                response["message"] = "There was some problem while getting the data."
                response["detail"] = f"{e}"
                print(f"ERROR: \n{e}")

            return response, 400


class DataSet(Resource):
    """This resource returns the stocks available for this dataset."""

    def get(self, shortname):
        """GET response."""

        # Prepare the response
        response = {}

        try:
            # Get the stocks on this dataset
            data = datasets.get_dataset_detail(shortname)

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