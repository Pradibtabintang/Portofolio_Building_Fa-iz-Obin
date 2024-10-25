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

def analyze_sorting_algorithms(sizes: List[int], trials: int = 3):
    algorithms = {
        'Bubble Sort': SortingAlgorithms.bubble_sort,
        'Selection Sort': SortingAlgorithms.selection_sort,
        'Insertion Sort': SortingAlgorithms.insertion_sort,
        'Quick Sort': SortingAlgorithms.quick_sort,
        'Merge Sort': SortingAlgorithms.merge_sort
    }
    
    results = {name: [] for name in algorithms.keys()}

    for size in sizes:
        print(f"\nTesting with array size: {size}")
        
        for algo_name, algo_func in algorithms.items():
            total_time = 0
            
            for _ in range(trials):
                # Generate random array
                arr = [random.randint(1, 1000) for _ in range(size)]
                
                # Measure sorting time
                start_time = time.time()
                sorted_arr = algo_func(arr)
                end_time = time.time()
                
                total_time += (end_time - start_time)
                
            avg_time = total_time / trials
            results[algo_name].append(avg_time)
            print(f"{algo_name}: {avg_time:.6f} seconds")
    
    return results
def plot_results(sizes: List[int], results: dict):
    plt.figure(figsize=(12, 6))
    
    for algo_name, times in results.items():
        plt.plot(sizes, times, marker='o', label=algo_name)
    
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Performance Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Test dengan berbagai ukuran array
    sizes = [100, 500, 1000, 2000, 3000]
    results = analyze_sorting_algorithms(sizes)
    plot_results(sizes, results)

main()
