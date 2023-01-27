#!/usr/bin/env python3
"""
This module contains LIFO Caching implementation
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFO Caching implementation
    """
    def __init__(self):
        """class instantiation constructor"""
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """
        add an item into a cache
        Args:
            key(str): key of the item
            item: item to be added
        Returns: None
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key_2nd_last = len(self.cache_data_list) - 2
                key_last = self.cache_data_list.pop(key_2nd_last)
                del self.cache_data[key_last]
                print("DISCARD: {}".format(key_last))

    def get(self, key):
        """retrieve an item
        Args:
            key(str): key of the item to search
        Returns: item if key exists. None otherwise
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
