#!/usr/bin/env python3
""" Module for using PyMongo to parse nginx logs """

from pymongo import MongoClient


# default host:port is localhost:27017
client = MongoClient()
collection = client.logs.nginx

# have to use empty {} to get count of all docs!
count = collection.count_documents({})
get = collection.count_documents({"method": "GET"})
post = collection.count_documents({"method": "POST"})
put = collection.count_documents({"method": "PUT"})
patch = collection.count_documents({"method": "PATCH"})
delete = collection.count_documents({"method": "DELETE"})
status = collection.count_documents({"method": "GET", "path": "/status"})

if __name__ == "__main__":
    print(f"{count} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{status} status check")