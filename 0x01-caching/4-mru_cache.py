#!/usr/bin/env python3
"""
Module that defines a FIFO cache system.
"""


class BaseCaching:
    """
    BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """
        Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """
        Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """
        Add an item in the cache
        """
        raise Exception("Method not implemented")

    def get(self, key):
        """
        Get an item by key
        """
        raise Exception("Method not implemented")


class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that inherits from
    BaseCaching and implements the MRU caching algorithm.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Add an item to the cache.
        If the cache exceeds 'MAX_ITEMS', the most recently
        used item is discarded.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.key_order.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    discarded = self.key_order.pop(0)
                    del self.cache_data[discarded]
                    print(f"DISCARD: {discarded}")
            self.cache_data[key] = item
            self.key_order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        Returns None if key is None or key is not in the cache.
        """
        if key is not None and key in self.cache_data:
            self.key_order.remove(key)
            self.key_order.append(key)
            return self.cache_data[key]
        return None
