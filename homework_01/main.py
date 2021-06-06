"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    squared_numbers = []
    for num in args:
        squared_numbers.append(num ** 2)
    return squared_numbers


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def even_numbers(num):
    return num % 2 == 0

def odd_numbers(num):
    return num % 2 != 0

def is_prime(num):
    divider = 2
    if num > 1:
        while divider ** 2 <= num and num % divider != 0:
            divider += 1
        return divider ** 2 > num

def filter_numbers(int_num, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_type == 'even':
        return list(filter(even_numbers, int_num))
    elif filter_type == 'odd':
        return list(filter(odd_numbers, int_num))
    elif filter_type == 'prime':
        return list(filter(is_prime, int_num))


if __name__ == '__main__':
    print('-------------------- Task #1 ----------------------------------')
    print(power_numbers(1, 2, 5, 7), '\n')

    print('-------------------- Task #2 ----------------------------------')
    print(filter_numbers([2, 3, 4, 5], EVEN))
    print(filter_numbers([1, 2, 3], ODD))
    print(filter_numbers([6, 3, -12, 7, 55, 90], PRIME))
