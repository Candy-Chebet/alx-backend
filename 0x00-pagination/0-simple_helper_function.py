#!/usr/bin/env python3
"""
This module contains a function that takes two integer arguments page and
 page_size and returns a tuple of size two containing start and end index"
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """this method takes two args and returns tuple of size two containing
    the start and end indices corresponding to the range of indices to return
    in a list for those particular pagination parameters
    Args:
        page(int): page number to return
        page_size(int): number of items per page
    Return: tuple(start, end)
    """
    start = 0
    end = 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
