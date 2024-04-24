import random

lst = [random.randint(1, 15) for i in range(10)]
print(lst)


def bubble_sort(arr):
    long_arr = len(arr)
    for index in range(long_arr - 1):
        current_element = arr[index]
        next_element = arr[index + 1]
        if current_element >= next_element:
            arr[index], arr[index + 1] = arr[index + 1], arr[index]
        for index in range(long_arr - 1):
            current_element = arr[index]
            next_element = arr[index + 1]
            if current_element >= next_element:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
    return print(arr)


if __name__ == "__main__":
    bubble_sort(lst)
