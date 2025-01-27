#!/usr/bin/env python3
""" Module for using PyMongo to parse nginx logs """

from pymongo import MongoClient


# default host:port is localhost:27017
client = MongoClient()
collection = client.logs.nginx

# Count total logs
total_logs = collection.count_documents({})

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {}
for method in methods:
    method_counts[method] = collection.count_documents({"method": method})

get_status_count = collection.count_documents({"method": "GET", "path": "/status"})

if __name__ == "__main__":
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\t{method}: {method_counts[method]}")
    print(f"GET method and /status path: {get_status_count}")