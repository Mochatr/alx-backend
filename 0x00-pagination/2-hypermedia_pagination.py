#!/usr/bin/env python3
import csv
from typing import List, Tuple
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for a given
    page and page_size.

    Args:
       page (int): The current page number (1-indexed).
       page_size (int): The number of items per page.

    Returns:
       Tuple[int, int]: A tuple containing the start
                        index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular
    baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page from the dataset.

        Args:
           page (int): The current page number (1-indexed).
           page_size (int): The number of items per page.

        Returns:
           List[List]: A list of rows for the requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Get a page from the dataset with hypermedia metadata.

        Args:
          page (int): The current page number (1-indexed)
          page_size (int): The number of items per page

        Returns:
          Dict[str, Any]: A dictionary containing the dataset page
          and metadata.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }


if __name__ == "__main__":
    server = Server()
    print(server.get_page(1, 10))
    print(server.get_page(2, 10))
    print(server.get_hyper(1, 10))
    print(server.get_hyper(2, 10))
