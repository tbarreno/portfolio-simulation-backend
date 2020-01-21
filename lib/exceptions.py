#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Custom exceptions.
#

class ResourceNotFoundException(Exception):
    """The resource element (file or directory) was not found.
    It only has a explanatory message."""

    def __init__(self, message):
        """Initialization: sets the message."""
        self.message = message
