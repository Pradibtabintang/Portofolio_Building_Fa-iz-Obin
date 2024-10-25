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

    @staticmethod
    def selection_sort(arr: List[int]) -> List[int]:
        n = len(arr)
        arr = arr.copy()
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    
    @staticmethod
    def insertion_sort(arr: List[int]) -> List[int]:
        arr = arr.copy()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr
    @staticmethod
    def quick_sort(arr: List[int]) -> List[int]:
        arr = arr.copy()
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = [x for x in arr[1:] if x <= pivot]
            greater = [x for x in arr[1:] if x > pivot]
            return SortingAlgorithms.quick_sort(less) + [pivot] + SortingAlgorithms.quick_sort(greater)
    @staticmethod
    def merge_sort(arr: List[int]) -> List[int]:
        arr = arr.copy()
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        left = SortingAlgorithms.merge_sort(left)
        right = SortingAlgorithms.merge_sort(right)
        
        return SortingAlgorithms.merge(left, right)
    
    @staticmethod
    def merge(left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
