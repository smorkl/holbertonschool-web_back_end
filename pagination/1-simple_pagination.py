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
        try:
            page = int(page)
            page_size = int(page_size)
        except ValueError:
            # Manejar el caso en que las entradas no son números enteros válidos
            raise ValueError("Page and page size must be integers")
        assert page > 0, "Page number must be greater than 0"
        assert page_size > 0, "Page size must be greater than 0"

        indexes = self.index_range(page, page_size)
        data = self.dataset()

        return data[indexes[0] : indexes[1]]
