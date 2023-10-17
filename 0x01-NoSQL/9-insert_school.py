#!/usr/bin/env python3
"""
Inserts a new document to an existing collection
based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Adds a new document to collection
    Returns the new id
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
