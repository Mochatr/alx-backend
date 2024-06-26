#!/usr/bin/env python3
"""
Module that defines a FIFO cache system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that inherits from
    BaseCaching and implements the FIFO caching algorithm.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item to the cache.
        If the cache exceeds 'MAX_ITEMS', the first item put in
        the cache is discarded.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded = self.queue.pop(0)
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        Returns None if key is None or key is not in the cache.
        """
        return self.cache_data.get(key) if key is not None else None
