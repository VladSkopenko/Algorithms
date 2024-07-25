import random

from time_decor import timer

lst = [random.randint(1, 10) for i in range(5000)]


@timer
def insertion_sort(arr: list) -> list:
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp
    return arr


if __name__ == "__main__":
    insertion_sort(lst)
