"""
Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
be [2, 3, 6].

Follow-up: what if you can't use division?
"""
import math
from typing import List


def multiply_array_items_without_self(input_array: List[int]) -> List[int]:
    array_product = math.prod(input_array)

    return [int(array_product / value) for value in input_array]


def multiply_array_items_without_self_no_division(input_array: List[int]) \
        -> List[int]:
    # Factors left of index i and right of index make the product for at
    # index i. Multiplication of left and right factors will yield the product
    # without factor at index i.
    n = len(input_array)
    left = [1] * n
    right = [1] * n

    # Construct the array with the factors left of index i
    for i in range(1, n):
        left[i] = input_array[i - 1] * left[i - 1]

    # Construct the array with the factors right of index i
    for j in range(n - 2, -1, -1):
        right[j] = input_array[j + 1] * right[j + 1]

    # Construct the array with the resulting product at index i
    products = [lf * rf for lf, rf in zip(left, right)]

    return products
