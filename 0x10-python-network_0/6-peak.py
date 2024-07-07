#!/usr/bin/python3
"""Defines a peak-finding algorithm."""

def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    # Check if the list is empty
    if list_of_integers == []:
        return None

    # Get the size_of_list of the list
    size_of_list = len(list_of_integers)
    
    # If there's only one element, return it as the peak
    if size_of_list == 1:
        return list_of_integers[0]
    # If there are two elements, return the maximum of the two as the peak
    elif size_of_list == 2:
        return max(list_of_integers)

    # Find the mid_idle index
    mid_i = int(size_of_list / 2)
    peak = list_of_integers[mid_i]
    
    # Check if the mid_idle element is greater than its neighbors
    if peak > list_of_integers[mid_i - 1] and peak > list_of_integers[mid_i + 1]:
        return peak
    # If the mid_idle element is less than the element to its left,
    # recursively search the left half of the list
    elif peak < list_of_integers[mid_i - 1]:
        return find_peak(list_of_integers[:mid_i])
    # Otherwise, recursively search the right half of the list
    else:
        return find_peak(list_of_integers[mid_i + 1:])

