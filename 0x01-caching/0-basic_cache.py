#!/usr/bin/env python3
"""
Module that defines a basic cache system
"""


class BaseCaching:
    """
      BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """Initialize"""
        self.cache_data = {}

    def print_cache(self):
        """Print the cache"""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Add an item in the cache"""
        raise NotImplementedError("put must be implemented in
                                  your cache class")

    def get(self, key):
        """Get an item by key"""
        raise NotImplementedError("get must be implemented
                                  in your cache class")


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
