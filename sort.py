#!/usr/bin/env python3
"""
Simple sorting program that sorts numbers from command line arguments or standard input.
"""

import sys


def bubble_sort(arr):
    """
    Sort an array using the bubble sort algorithm.
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
    """
    n = len(arr)
    arr_copy = arr.copy()
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        if not swapped:
            break
    
    return arr_copy


def quick_sort(arr):
    """
    Sort an array using the quicksort algorithm.
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def main():
    """Main function to handle input and sorting."""
    if len(sys.argv) > 1:
        # Get numbers from command line arguments
        try:
            numbers = [float(arg) for arg in sys.argv[1:]]
        except ValueError:
            print("Error: All arguments must be valid numbers", file=sys.stderr)
            sys.exit(1)
    else:
        # Read from standard input
        print("Enter numbers separated by spaces or newlines (Ctrl+D to finish):")
        try:
            input_text = sys.stdin.read()
            numbers = [float(x) for x in input_text.split()]
        except ValueError:
            print("Error: All inputs must be valid numbers", file=sys.stderr)
            sys.exit(1)
    
    if not numbers:
        print("Error: No numbers provided", file=sys.stderr)
        sys.exit(1)
    
    # Sort using quicksort (faster for larger lists)
    sorted_numbers = quick_sort(numbers)
    
    # Print sorted numbers
    for num in sorted_numbers:
        # Print integers without decimal point
        if num == int(num):
            print(int(num))
        else:
            print(num)


if __name__ == "__main__":
    main()
