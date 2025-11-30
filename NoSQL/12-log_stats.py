#!/usr/bin/env python3
"""
Log stats
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    
    # Total logs
    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))
    
    # Methods
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    
    # Status check
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_count))
