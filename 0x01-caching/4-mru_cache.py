#!/usr/bin/env python3
"""
this module contains MRUCache tat inherits from BaseCaching and is
 a caching sysytem
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU Caching System"""
    def __init__(self):
        """
        instantiation of MRUCache class
        """
        super().__init__()
        self.cache_data_order = []

    def put(self, key, item):
        """
        add an item to a cache system
        Args:
           key(str): key of the item to add
           item(str): the item to add
        Returns: item if it is in the cache and None otherwise
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.cache_data_order:
                self.cache_data_order.append(key)
            else:
                self.cache_data_order.remove(key)
                self.cache_data_order.append(key)
            if len(self.cache_data_order) > BaseCaching.MAX_ITEMS:
                length_c = len(self.cache_data_order)
                popped = self.cache_data_order.pop(length_c - 2)
                del self.cache_data[popped]
                print("DISCARD: {}".format(str(popped)))

    def get(self, key):
        """
        retrieve an item from cache
        Args:
            key(str): key of the item to return it
        Returns: item if keu exists and None otherwise
        """
        if key in self.cache_data:
            self.cache_data_order.remove(key)
            self.cache_data_order.append(key)
            return self.cache_data[key]
        return None
