#!/usr/bin/env python3
import csv
import math
from typing import List


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


    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of data.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: The list of rows for the given page.
        """
        # Validate inputs
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        # Get dataset and slice based on index_range
        dataset = self.dataset()
        start, end = self.index_range(page, page_size)
        return dataset[start:end] if start < len(dataset) else []
