#!/usr/bin/env python3
"""
Module for paginating a dataset of popular baby names.

This module includes a function for calculating index ranges for pagination
and a `Server` class that provides methods to load and paginate a dataset
stored in a CSV file.
"""
import csv
from math import ceil
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of data.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: The list of rows for the given page.
        """
        assert isinstance(page, int) and page > 0, (
            "Page must be a positive integer."
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "Page size must be a positive integer."
        )

        dataset = self.dataset()
        start, end = index_range(page, page_size)
        return dataset[start:end] if start < len(dataset) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Generates a hypermedia-style pagination dictionary.

        Args:
            page (int): The current page number (1-indexed). Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            dict: A dictionary containing pagination details, including:
                - page_size (int): The number of items per page.
                - page (int): The current page number.
                - data (List): The list of items on the current page.
                - next_page (int | None): The next page number, or
                  None if it's the last page.
                - prev_page (int | None): The previous page number, or
                  None if it's the first page.
                - total_pages (int): The total number of pages.
        """
        total_pages = ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        data = {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
        return data
