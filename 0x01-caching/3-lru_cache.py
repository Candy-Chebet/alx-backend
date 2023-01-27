#!/usr/bin/env python3
"""
This module contains an implementation of an LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU Cache implemention - LRU class
    """
    def __init__(self):
        """instantiation of an LRUCache class"""
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """
        add an item into the cache
        Args:
            key(str): given key for the item
            item(str): item to be added
        Returns: None
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.cache_data_list:
                self.cache_data_list.append(key)
            else:
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                popped = self.cache_data_list.pop(0)
                del self.cache_data[popped]
                print("DISCARD: {}".format(popped))

    def get(self, key):
        """retrieve an item from cache
        Args:
            key(str): key of the item to be retrieved
        Returns: items - value of the item or None if key does not exist
        """
        if key:
            if key in self.cache_data:
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
                return self.cache_data[key]
        return None
