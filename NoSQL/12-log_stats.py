#!/usr/bin/env python3
""" Module for using PyMongo to parse Nginx logs in MongoDB """

from pymongo import MongoClient

# Connect to MongoDB server (default host:port is localhost:27017)
client = MongoClient()

# Select the 'nginx' collection in the 'logs' database
collection = client.logs.nginx

# Count the total number of documents in the collection
count = collection.count_documents({})

# Count the number of documents for each HTTP method
get = collection.count_documents({"method": "GET"})
post = collection.count_documents({"method": "POST"})
put = collection.count_documents({"method": "PUT"})
patch = collection.count_documents({"method": "PATCH"})
delete = collection.count_documents({"method": "DELETE"})

# Count the number of GET requests with the path '/status'
status = collection.count_documents({"method": "GET", "path": "/status"})

if __name__ == "__main__":
    # Print the total number of logs in the collection
    print(f"{count} logs")

    # Print the count for each HTTP method
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")

    # Print the count of GET requests with path '/status'
    print(f"{status} status check")
