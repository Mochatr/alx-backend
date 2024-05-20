#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""


import csv
from typing import List, Tuple
import math


class Server:
    """
    Server class to paginate a database of popular
    baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict[str, Any]:
        """
        Get a page from the indexed dataset with hypermedia
        metadata.

        Args:
           index (int): The start index of the return page.
           page_size (int): The number of items per page.

        Returns:
          Dict[str, Any]: A dictionary containing the dataset page
                          and metadata.

        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        indexed_keys = sorted(indexed_data.keys())

        data = []
        current_index = index
        next_index = None

        for _ in range(page_size):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                current_index += 1
            else:
                break

        if current_index < len(indexed_keys):
            next_index = current_index

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }


if __name__ == "__main__":
    server = Server()
    print(server.get_page(0, 10))
    print(server.get_page(10, 10))
