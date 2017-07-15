def find_smallest(arr):
    """Функция поиска индекса наименьшего элемента в массиве"""
    smallest = arr[0]  # Для хранения наименьшего элемента
    smallest_index = 0  # Для хранения индекса наименьшего элемента
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    """Функция сортировки массива"""
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)  # Находит наименьший элемент в массиве
        new_arr.append(arr.pop(smallest))  # Добавляет найденный элемент в новый массив
    return new_arr

print(selectionSort([5, 2, 10, 6, 3, 9, 1, 8]))



