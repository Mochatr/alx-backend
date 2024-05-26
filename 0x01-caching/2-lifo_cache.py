#!/usr/bin/env python3
""" Module that defines a FIFO cache system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache is a caching system that inherits from
    BaseCaching and implements the LIFO caching algorithm.
    """

    def __init__(self):
        """ Initialize the class.
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add an item to the cache.
        If the cache exceeds 'MAX_ITEMS', the last item put in
        the cache is discarded.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.stack.remove(key)
                self.stack.append(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    discarded = self.stack.pop()
                    del self.cache_data[discarded]
                    print(f"DISCARD: {discarded}")
                self.cache_data[key] = item
                self.stack.append(key)

    def get(self, key):
        """ Retrieve an item from the cache by key.
        Returns None if key is None or key is not in the cache.
        """
        return self.cache_data.get(key) if key is not None else None
