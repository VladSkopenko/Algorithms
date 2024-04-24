import random

from time_decor import timer

lst = [random.randint(1, 10) for i in range(50000)]
print(lst)


@timer
def bubble_sort(arr):
    long_arr = len(arr)
    for index in range(long_arr - 1):
        current_element = arr[index]
        next_element = arr[index + 1]
        if current_element >= next_element:
            arr[index], arr[index + 1] = arr[index + 1], arr[index]
        for index_ in range(long_arr - 1):
            current_element = arr[index_]
            next_element = arr[index_ + 1]
            if current_element >= next_element:
                arr[index_], arr[index_ + 1] = arr[index_ + 1], arr[index_]
    return print(arr)


if __name__ == "__main__":
    bubble_sort(lst)
