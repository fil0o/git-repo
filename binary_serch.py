def binary_serch(list, item):
    # В переменных low and high хранятся границы той части списка где выполнятся поиск
    low = 0
    high = len(list) - 1

    while low <= high:
        # Цикл работает пока список не сократится до одного элемента
        mid = low + high
        guess = list[mid]
        if guess == item:
            # Значение найдено
            return mid
        if guess > item:
            # Много
            high = mid - 1
        else:
            # Мало
            low = mid + 1
    return None     # Значение не найдено


my_list = [1, 3, 5, 7, 9]

print(binary_serch(my_list, 5))