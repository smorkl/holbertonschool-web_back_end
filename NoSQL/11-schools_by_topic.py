#!/usr/bin/env python3

"""
Module to interact with MongoDB collections.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Finds all documents in the collection where the 'topic' field
    matches the provided topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection object to search in.
        topic (str): The topic to search for in the 'topic' field of
        the documents.

    Returns:
        list: A list of documents where the 'topic'
        field matches the provided topic.
    """
    return [item for item in mongo_collection.find({"topics": topic})]