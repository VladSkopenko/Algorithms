import random

from time_decor import timer

lst = [random.randint(-5, 15) for i in range(50000)]


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


@timer
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = arr.index(min(arr))
        new_arr.append(arr.pop(smallest))
    return new_arr


if __name__ == "__main__":
    print(selection_sort(lst))
