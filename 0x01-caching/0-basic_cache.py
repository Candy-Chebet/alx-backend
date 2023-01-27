#!/usr/bin/env python3
"""
this module contains class BasicCache that inherits from BaseCaching and
 is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    basic caching system
    """
    def __init__(self):
        """
        initialize class instance
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        add an item to the caching system
        Args:
            key(str): key of the item to be added
            item(str): item to add to the cache
        Returns: None
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        get or retrieve an item from the cache system
        Args: key(str) key of the item to be retrieved from cache
        Returns: item associated with the key or None if the key is not in the
        cache or if the key is not given
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
