from time_decor import timer
import timeit

@timer
def binary_search(sort_list: list, item) -> int | None:
    low = 0
    high = len(sort_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sort_list[mid]
        if guess == item:
            return mid
        if guess >= item:
            high = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == "__main__":
    data = [i for i in range(9000000)]
    print(binary_search(data, 12))
    execution_time = timeit.timeit(lambda: binary_search(data, 50), number=1)
    print("Час виконання: ", execution_time)
