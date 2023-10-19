#!/usr/bin/env python3
"""
This module contains a Python script that provides stats about Nginx logs
stored in MongoDB.

Database: logs
Collection: nginx
Display (with this format):
    First line: x logs where x is the number of documents in this collection.
    Second line: Methods:
    5 lines with the number of documents with the
        method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        in this order (add a tab before each line).
    One line with the number of documents with:
        method=GET
        path=/status
"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """
    Provides stats about Nginx logs stored in MongoDB
    """
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        documents = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {documents}")

    status_get = mongo_collection.count_documents({"method": "GET"},
                                                  {"path": "/status"})
    print(f"{status_get} status check")


if __name__ == "__main__":
    with MongoClient() as client:
        collection = client.logs.nginx
        log_stats(collection)
