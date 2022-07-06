from typing import List

class Sorter:
    def sort(self, array: List) -> List:
        raise NotImplementedError()

    @staticmethod
    def swap(array: List, idx1: int, idx2: int) -> None:
        array[idx1], array[idx2] = array[idx2], array[idx1]