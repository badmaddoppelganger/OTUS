"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args: int) -> list:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    return [i ** 2 for i in args]


def is_prime(digit: int):
    """method return that the digit is prime or not
    """
    if digit in [0, 1]:
        return False
#    return not any(num for num in range(2, int(digit / 2) + 1) if digit % num == 0)
    for num in range(2, int(digit / 2) + 1):
        if (digit % num) == 0:
            return False
    return True


def is_odd(digit: int) -> int:
    """method return that the digit is odd or not
    """
    return digit & 1


def is_even(digit: int) -> bool:
    """method return that the digit is odd or not
    """
    return not digit & 1


# filter types (PEP8 E731 do not assign a lambda expression, use a def!)
ODD = is_odd
EVEN = is_even
PRIME = is_prime


def filter_numbers(lst: list[int], func) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    return list(filter(func, lst))
