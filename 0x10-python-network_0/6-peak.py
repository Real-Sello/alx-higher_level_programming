#!/usr/bin/python3
"""Program that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    A peak is defined as an element that is greater than its neighbors.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: A peak element, or None if the list is empty.

    Complexity:
        The complexity of this algorithm is O(log(n)), where n is the length of the list.
        The algorithm utilizes a binary search approach to find a peak element efficiently.
    """

    if not list_of_integers:  # Check if the list is empty
        return None

    size = len(list_of_integers)
    start = 0
    end = size - 1

    while start < end:
        mid = (start + end) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            start = mid + 1
        else:
            end = mid

    return list_of_integers[start]

