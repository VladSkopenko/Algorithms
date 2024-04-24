import random

from time_decor import timer

lst = [random.randint(1, 10) for i in range(5000)]


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
    length_of_list = len(arr)
    for index in range(length_of_list - 1):
        if arr[index] >= arr[index + 1]:
            arr[index], arr[index + 1] = arr[index + 1], arr[index]

        for index_ in range(length_of_list - 1):
            if arr[index_] >= arr[index_ + 1]:
                arr[index_], arr[index_ + 1] = arr[index_ + 1], arr[index_]
    return print(arr)


if __name__ == "__main__":
    bubble_sort(lst)
