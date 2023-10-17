#!/usr/bin/env python3
"""
Lists all documents in Mongodb collection.
"""


def list_all(mongo_collection):
    """
    Returns a list of documents in the collection given,
    or an empty list if no documents are found.
    """
    if mongo_collection:
        return [doc for doc in mongo_collection.find()]
    else:
        return []
