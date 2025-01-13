#!/usr/bin/env python3

def update_topics(mongo_collection, name, topics):
    """
    Updates the topics list for a school document in the given collection.

    Args:
        mongo_collection: The pymongo collection object representing the school collection.
        name (str): The name of the school document to update.
        topics (list): The new list of topics to be assigned to the school.

    Returns:
        The number of documents updated (usually 1 if successful).

    Raises:
        TypeError: If any of the arguments have unexpected types.
    """

    if not isinstance(mongo_collection, pymongo.collection.Collection):
        raise TypeError("mongo_collection must be a pymongo.collection.Collection object.")
    if not isinstance(name, str):
        raise TypeError("name must be a string.")
    if not isinstance(topics, list):
        raise TypeError("topics must be a list of strings.")

    # Update the document using a filter and update operator
    result = mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}}
    )
    return result.modified_count