from Ejercicios_Funciones import is_prime, find_prime_numbers
import pytest

#prime_number
def test_is_prime_with_prime_number():
    assert is_prime(13) is True


def test_is_prime_with_non_prime_number():
    assert is_prime(10) is False


def test_is_prime_with_string():
    with pytest.raises(TypeError):
        is_prime("hello")


#find_prime_numbers
def test_find_prime_numbers_with_negatives():
    test_list = [-10, -3, -1, 0, 1, 2, 3]

    assert find_prime_numbers(test_list) == [2, 3]


def test_find_prime_numbers_empty_list():
    assert find_prime_numbers([]) == []


def test_find_prime_numbers_with_mixed_types():
    test_list = [2, "a", 5, "hello", 7]

    with pytest.raises(TypeError):
        find_prime_numbers(test_list)
