#!/usr/bin/env python3

"""
This module contains a function to update the 'topics' field in all documents
within a MongoDB collection that match a given school name.

Function:
    update_topics(mongo_collection, name, topics)
        Updates the 'topics' field of documents that match the given 'name' in
        the MongoDB collection.

Parameters:
    mongo_collection (pymongo.collection.Collection): The MongoDB collection
    name (str): The name of the school to search for in the collection
    topics (list of str): A list of topics to set for the specified school
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the school name.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )