import random

from time_decor import timer

lst = [random.randint(1, 10) for i in range(10000)]


@timer
def bubble_sort(arr):
    """
    O(n) ** 2 найгірша
    O(n) найкраща
    Для масива
    Стабильно
    Учбовий алгоритм
    :param arr: list
    :return: list
    """
    length_of_list = len(arr) - 1
    for _ in range(length_of_list):
        for index in range(length_of_list):
            if arr[index] >= arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
    return print(arr)


if __name__ == "__main__":
    bubble_sort(lst)
