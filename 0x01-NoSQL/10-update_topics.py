#!/usr/bin/env python3
"""
This module contains a function that changes all topics of a school document
based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    Args:
        mongo_collection: pymongo collection object
        name(str) school name to update
        topics(all str) list of topics
    """
    new_docs = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return new_docs
