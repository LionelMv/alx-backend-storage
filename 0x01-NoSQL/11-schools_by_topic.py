#!/usr/bin/env python3
"""
This module contains a function that returns the list of school
having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic.
    Args:
        mongo_collection: pymongo collection object
        topic(str): topic searched
    """
    # return mongo_collection.find({"topic": {"$in": topic}})
    return mongo_collection.find({"topics": topic})
