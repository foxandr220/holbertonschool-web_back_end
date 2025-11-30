#!/usr/bin/env python3
"""
Where can I learn Python?
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic
    
    Args:
        mongo_collection: pymongo collection object
        topic (string): topic searched
        
    Returns:
        List of school documents that have the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))
