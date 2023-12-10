import random


def generate_random_array(size: int, min: int, max: int) -> list:
    """
    Описание:
    Функция генерирует массив случайных чисел заданного размера в заданном диапазоне.

    Аргументы:
    - size (int): Размер массива.
    - min (int): Минимальное значение элемента массива.
    - max (int): Максимальное значение элемента массива.

    Возвращает:
    - list: Список случайных чисел заданного размера в заданном диапазоне.
    """
    return [random.randint(min, max) for _ in range(size)]
