#!/usr/bin/env python3
""" Module for using PyMongo to parse nginx logs """

from pymongo import MongoClient

# Establish connection to the MongoDB server
client = MongoClient()

# Access the 'logs' database and 'nginx' collection
col = client.logs.nginx

# Count the total number of documents in the 'nginx' collection
count = col.count_documents({})

# Count the number of documents for each HTTP method (GET, POST, PUT, PATCH, DELETE)
get = col.count_documents({"method": "GET"})
post = col.count_documents({"method": "POST"})
put = col.count_documents({"method": "PUT"})
patch = col.count_documents({"method": "PATCH"})
delete = col.count_documents({"method": "DELETE"})

# Count the number of GET requests where the path is "/status"
status = col.count_documents({"method": "GET", "path": "/status"})

# Print the stats in the required format
if __name__ == "__main__":
    print(f"{count} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{status} status check")
