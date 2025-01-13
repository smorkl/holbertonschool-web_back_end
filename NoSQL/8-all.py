#!/usr/bin/env python3
"""List all documents in Python"""


def list_all(mongo_collection):
    """
    Lists all documents in a given MongoDB collection.

    Args:
        mongo_collection: The pymongo.collection.Collection object representing 
                          the MongoDB collection to list.

    Returns:
        A list of dictionaries, where each dictionary represents a document 
        in the collection. If the collection is None, an empty list is returned.
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find())