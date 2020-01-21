#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Resource module for backend information.
#

from flask_restful import Resource

class BackendInformation(Resource):
    """This resource just returns the current backend version."""

    def get(self):
        """GET response."""
        return {'version': '1.0.0'}
