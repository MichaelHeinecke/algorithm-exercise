"""
Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

from typing import List


def sum_of_array_items_equals_number(array: List[int], number: int) -> bool:
    visited_items = set()
    for item in array:
        if number - item in visited_items:
            return True
        visited_items.add(item)

    return False
