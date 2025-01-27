#!/usr/bin/env python3
""" Module for using PyMongo to parse nginx logs """

from pymongo import MongoClient


# default host:port is localhost:27017
client = MongoClient()
collection = client.logs.nginx

# Count total logs
total_logs = collection.count_documents({})

# List of HTTP methods to check
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: 0 for method in methods}  # Initialize method counts

# Count documents for each method
for method in methods:
    method_counts[method] = collection.count_documents({"method": method})

# Count GET method with /status path
get_status_count = collection.count_documents({"method": "GET", "path": "/status"})

if __name__ == "__main__":
    # Print total number of logs
    print(f"{total_logs} logs")
    
    # Print method counts
    print("Methods:")
    for method in methods:
        print(f"\t{method}: {method_counts[method]}")
    
    # Print GET /status count
    print(f"GET method and /status path: {get_status_count}")
