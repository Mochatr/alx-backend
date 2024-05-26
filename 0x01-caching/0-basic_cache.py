#!/usr/bin/env python3
"""
Module that defines a basic cache system.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a simple caching system
    the inherits from BaseCaching.
    It does not limit the size of the cache.
    """

    def put(self, key, item):
        """
        Add an item to the cache.
        If key or item in None, does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        Returns None if key is None or key is not
        in the cache.
        """
        return self.cache_data.get(key) if key is not None else None
