def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Инициализируем счетный массив
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)

    # Считаем количество каждого элемента в исходном массиве
    for num in arr:
        count_arr[num - min_val] += 1

    # Изменяем счетный массив так, чтобы каждый элемент содержал сумму предыдущих
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # Строим отсортированный массив
    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_val] - 1] = arr[i]
        count_arr[arr[i] - min_val] -= 1

    return output_arr

# Пример использования
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Отсортированный массив:", sorted_arr)