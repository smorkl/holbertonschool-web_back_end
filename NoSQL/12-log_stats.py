#!/usr/bin/env python3
"""
Log statistics retrieval.

This script connects to a MongoDB instance to retrieve and display statistics
about Nginx logs stored in a collection. It provides the total number of logs,
the counts of logs per HTTP method, and the number of GET requests with the 
path '/status'.
"""

from pymongo import MongoClient


def logs_stats(query):
    """
    Count the number of documents in the logs collection that match the given query.

    Keyword arguments:
    query -- a dictionary specifying the conditions to match in the MongoDB collection.
    
    Return:
    An integer representing the number of documents that match the query.
    """
    
    # Connect to the MongoDB server running locally (default port 27017)
    client = MongoClient('mongodb://localhost:27017/')  # Adjust the connection string if needed
    logs = client.logs.nginx  # Access the 'nginx' collection within the 'logs' database
    return logs.count_documents(query)  # Return the count of matching documents


def main():
    """
    Main function to connect to MongoDB, retrieve Nginx log statistics, 
    and display the results in a specified format.
    """
    
    # List of HTTP methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    # Print total number of logs
    print(f"{logs_stats({})} logs")
    
    # Print header for HTTP method counts
    print("Methods:")
    
    # Iterate over the methods and print the count for each
    for method in methods:
        print(f"\tmethod {method}: {logs_stats({'method': method})}")
    
    # Print the count of GET requests with the path '/status'
    print(f"{logs_stats({'method': 'GET', 'path': '/status'})} status check")
    

if __name__ == "__main__":
    main()  # Call the main function to run the script
