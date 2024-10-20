"""
    Given a list of sorted integers, square the elements and give the output
    in sorted order.
    Brute Force: Square all the elements and sort the list.
"""


def sorted_squarred(arr):
    n = len(arr)
    new_array = [0] * n

    for i in range(n):
        new_array[i] = arr[i] ** 2

    new_array.sort()
    return new_array


print(sorted_squarred([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]


# Version simplifier

def sorted_squarredV2(arr):
    n = len(arr)
    i, j = 0, n - 1
    new_array = [0] * n

    for k in reversed(range(n)):
        if arr[i] ** 2 > arr[j] ** 2:
            new_array[k] = arr[i] ** 2
            i += 1
        else:
            new_array[k] = arr[j] ** 2
            j -= 1

    return new_array


print(sorted_squarredV2([-40, -41, 0, 3, 10]))  # [0, 1, 9, 16, 100]
