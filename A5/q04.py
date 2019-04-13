import doctest


def selection_sort(unsorted: list):
    """Return a sorted copy of sortable_items.

    PRECONDITION sortable_items must be a non-empty list
    PRECONDITION elements in sortable items must be of the same type
    RETURN sorted copy
    >>> selection_sort([1, 8, 9, 2])
    [1, 2, 8, 9]
    >>> selection_sort(["z", "d", "a", "g"])
    ['a', 'd', 'g', 'z']"""
    if len(unsorted) <= 0:
        raise ValueError("Please enter a list that is non-empty.")

    sorted_copy = unsorted[:]
    for i in range(len(sorted_copy)):
        minimum = sorted_copy[i]
        location = i
        for j in range(i, len(sorted_copy)):
            if sorted_copy[j] < minimum:
                minimum = sorted_copy[j]
                location = j
        sorted_copy[location], sorted_copy[i] = sorted_copy[i], sorted_copy[location]
    return sorted_copy


def main():
    doctest.testmod()


if __name__== '__main__':
    main()
