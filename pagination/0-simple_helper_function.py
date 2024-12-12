#!/usr/bin/env python3
"""
This module has a function that returns
the start and end index of a page.
fuction:
    index_range(page: int, page_size: int): The function
    returns the start and end index based on
    the requested page and the page size
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    The function returns the start and end index based
    on the requested page and the page size
    arg:
        page(int): Requested page number
        page_size(int): page content size
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
