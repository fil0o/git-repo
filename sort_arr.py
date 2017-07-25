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

print(selectionSort([5, 2, 10, 6, 3, 9, 1, 12, 26]))

def quick_sort(array):
    if len(array) < 2:  # Базовый случай: массива с 0 и 1 элементом уже отсортированы
        return array
    else:
        pivot = array[0]  # Рекурсивный случай

        less = [i for i in array[1:] if i <= pivot]  # Подмассив всех элементов, меньше опорного
        greater = [i for i in array[1:] if i > pivot]  # Подмассив всех элементов, больше опорного

        return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([5, 2, 10, 6, 3, 9, 1, 12, 26]))





