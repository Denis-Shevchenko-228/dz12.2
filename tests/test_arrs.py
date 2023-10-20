from utils import arrs


def test_get():
    # Тест со списком целых чисел
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3], 0, "test") == 1
    # Тест со списком строк
    assert arrs.get(["a", "b", "c"], 1, "test") == "b"
    assert arrs.get(["a", "b", "c"], 0, "test") == "a"
    # Тест с пустым списком
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([], 1, "test") == "test"
    # тест со списком смешанных типов
    assert arrs.get([1, "b", 3.0], 1, "test") == "b"
    assert arrs.get([1, "b", 3.0], 0, "test") == 1
    # Тест с отрицательным индексом
    assert arrs.get([1, 2, 3], -1, "test") == "test"

    # Тест с индексом вне диапазона
    assert arrs.get([1, 2, 3], 5, "test") == "test"
    assert arrs.get([1, 2, 3], -5, "test") == "test"


def test_slice():
    # Тест с начальным и конечным индексами
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], 1) == [2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4]) == [1, 2, 3, 4]

    # Тест только с начальным индексом
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1, 3) == [2, 3]

    # Тест с отрицательными индексами
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, -1) == [3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], -3) == [3, 4, 5]

    # Тест с начальным индексом больше длины массива
    assert arrs.my_slice([1, 2, 3], 5) == []
    assert arrs.my_slice([1, 2, 3], 5, 7) == []

    # Тест с конечным индексом больше длины массива
    assert arrs.my_slice([1, 2, 3], 1, 5) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1, 7) == [2, 3]

    # Тест с начальным индексом равным конечному индексу
    assert arrs.my_slice([1, 2, 3], 1, 1) == []

    # Тест с пустым массивом
    assert arrs.my_slice([], 1, 3) == []
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([]) == []
