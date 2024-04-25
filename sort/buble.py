import random

from time_decor import timer

lst = [random.randint(1, 10) for i in range(5000)]


@timer
def bubble_sort(arr):
    """
    O(n) ** 2 найгірша
    O(n) найкраща
    Для масива, списка
    Стабільний, однакові елементи зберігають свої позиції відносно один одного
    Учбовий алгоритм
    :param arr: list
    :return: list
    """
    length_of_list = len(arr) - 1
    for n_iter in range(length_of_list):
        for index in range(length_of_list - n_iter):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
    return print(arr)


if __name__ == "__main__":
    bubble_sort(lst)
