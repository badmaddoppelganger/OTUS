"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    up_sqrt = [i ** 2 for i in args]
    return up_sqrt


def is_prime(digit):
    """method that return that the digit is prime or not
    """
    for a in range(2, digit):
        if (digit % a) == 0:
            return False
    else:
        return True


def is_odd(digit):
    """method that return that the digit is odd or not
    """
    return digit % 2 == 1


def is_even(digit):
    """method that return that the digit is odd or not
    """
    return digit % 2 == 0


# filter types
ODD = is_odd
EVEN = is_even
PRIME = is_prime


def filter_numbers(lst, func):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    result = filter(func, lst)
    return result
