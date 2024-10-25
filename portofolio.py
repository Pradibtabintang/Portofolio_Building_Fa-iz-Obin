import random
import time
import matplotlib.pyplot as plt
from typing import List


class SortingAlgorithms:
    @staticmethod
    def bubble_sort(arr: List[int]) -> List[int]:
        n = len(arr)
        arr = arr.copy()
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
