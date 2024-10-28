# Sorting Algorithms Visualization

A Python implementation and performance analysis tool for common sorting algorithms. This project provides a visual comparison of different sorting algorithms' time complexity through practical benchmarking.

## Authors
This project was collaboratively developed by:

Muhammad Fa'iz Ismail (@Faizism)
Pradibta Bintang Maulana (@Pradibtabintang)

We believe in the power of collaboration and how different perspectives can create better software. Feel free to reach out to either of us with questions or suggestions!

## Features

* Implementation of 5 classic sorting algorithms:
  * Bubble Sort
  * Selection Sort
  * Insertion Sort
  * Quick Sort
  * Merge Sort
* Performance analysis with customizable array sizes
* Multiple trials for accurate averaging
* Visualization of performance metrics using matplotlip
* Type-annotated code for better maintainability

## Requirements
* Python 3.12 or later
* matplotlib 3.9 or later
* typing

## Installation
``` bash
pip install matplotlib
```

## Implementation Details
**Sorting Algorithm**
1. Bubble Sort
   * Compares adjacent elements and swaps them if they're in the wrong order
2. Selection Sort
   * Finds the minimum element and places it at the beginning
3. Insertion Sort
   * Builds the final sorted array one item at a time
4. Quick Sort
   * Uses divide-and-conquer strategy with a pivot element
5. Merge Sort
   * Divides array into two halves, recursively sorts them, and merges
  
## Analysis Features
* **Multiple Trials**: Each algorithm is run multiple times (default: 3) to get average performance
* **Various Array Sizes**: Tests performance across different input sizes
* **Random Data Generation**: Uses randomly generated arrays for realistic testing
* **Visual Comparison**: Generates a plot comparing all algorithms' performance

## Output
The program outputs:
1. Console logs showing execution time for each algorithm at different array sizes
2. A matplotlib graph displaying:
   * (X-axis: Array sizes
   * Y-axis: Execution time in seconds
   * Different colored lines for each sorting algorithm
  
## Contributing
Feel free to fork this repository and submit pull requests. You can:
* Add new sorting algorithms
* Improve existing implementations
* Add new visualization features
* Enhance performance analysis metric

## License
This project is open-source and available for educational and practical use.

## Note
The performance of these algorithms may vary based on:
* Hardware specifications
* System load
* Input data characteristics
* Python implementation (CPython, PyPy, etc.)
