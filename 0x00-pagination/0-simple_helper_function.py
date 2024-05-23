#!/usr/bin/env python3
"""
This module provides a utility function 'index range'
that calculates the start and end indices for pagination.
"""
from typing import Tuple


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


if __name__ == "__main__":
    print(index_range(1, 10))
    print(index_range(2, 10))
