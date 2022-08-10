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
    up_sqrt = [i**2 for i in args]
    return up_sqrt


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "is_prime"

def is_prime(digit):
    """method that return that the digit is prime or not
    >>> is_prime(5)
    <<< True
    """
    a = [False if (digit % i) == 0 else True for i in range(2, int(digit / 2))]
    return a

def filter_numbers():
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
