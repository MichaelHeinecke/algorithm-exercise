"""
Given an array of integers, find the first missing positive integer in linear time and
constant space. In other words, find the lowest positive integer that does not exist in
the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
from typing import List


def find_first_missing_integer_in_array(arr: List[int]) -> int:
    """
    Finds the first missing integer in an array.

    The algorithm leverages the fact that the solution of an array of length l must be
    within [1, ..., l] and performs the following steps to find the result:
    1. In a first pass over the array, all numbers > 0 and <= l are moved to their
       respective index (1 -> index 0, 2 -> index 1, etc.). All other numbers are not
       moved.
    2. In a second pass, the first number that doesn't match its index, is the first
       missing integer.

    :param arr: Input array.
    :return: First missing integer in input array.
    """
    # Step 1 - Move eligible numbers to their respective index
    l = len(arr)
    i = 0
    while i < l:
        correct_index = arr[i] - 1
        if 0 < arr[i] <= l and arr[i] != arr[arr[i] - 1]:
            temp = arr[i]
            arr[i] = arr[correct_index]
            arr[correct_index] = temp
        else:
            i += 1

    # Step 2 - Find first missing number in array
    for i in range(l):
        if arr[i] != i + 1:
            return i + 1

    return l + 1
