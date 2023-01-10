import os


def diskUsage(path):
    """
    Finding the usage of a folder or file in a specific location in the drive
    :param path: The path to the file or folder
    :return: The size of each file in the folder
    """
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for i in os.listdir(path):
            childPath = os.path.join(path, i)
            total += diskUsage(childPath)
    print('{0:<6}'.format(total), path)
    return total


def reverse(array, start, stop):
    """
    Reversing an array using recursion
    :param array:   The array to be reverse
    :param start:  The starting index
    :param stop:    The ending index
    :return: Another recursion until start is equal to stop-1
    """
    if start < stop - 1:
        array[start], array[stop - 1] = array[stop - 1], array[start]
        reverse(array, start + 1, stop - 1)
