import random

from time_decor import timer

lst = [random.randint(1, 10) for i in range(5000)]


@timer
def insert_sort(arr):
    length_of_list = len(arr)
    for start in range(1, length_of_list):
        for index in range(start, 0, -1):
            if arr[index] < arr[index - 1]:
                arr[index - 1], arr[index] = arr[index], arr[index - 1]
            else:
                break

    return print(arr)


if __name__ == "__main__":
    insert_sort(lst)
