from Bubble_Sort import bubble_sort
import pytest

def test_bubble_sort_with_small_list():
    assert bubble_sort([8,5,3,1,4,7,9]) == [1, 3, 4, 5, 7, 8, 9]

def test_bubble_sort_with_big_list():
    test_list = [
        42, 7, 89, 15, 63, 28, 91, 3, 76, 54,
        12, 99, 34, 67, 1, 80, 25, 58, 44, 73,
        19, 85, 6, 92, 31, 70, 14, 48, 60, 9,
        37, 82, 23, 95, 50, 11, 68, 2, 77, 33,
        56, 21, 90, 4, 72, 18, 64, 39, 87, 10,
        53, 26, 79, 5, 88, 30, 61, 16, 94, 40,
        74, 22, 83, 8, 69, 27, 97, 13, 52, 35,
        81, 17, 59, 46, 93, 24, 71, 36, 98, 20,
        66, 29, 84, 45, 100, 32, 75, 41, 96, 38,
        62, 47, 86, 43, 78, 49, 57, 65, 55, 51
    ]

    assert bubble_sort(test_list) == sorted(test_list)


def test_bubble_sort_with_empty_list():
    assert bubble_sort([]) == []


def test_bubble_sort_with_string_parameter():
    input_string = "Hello"
    with pytest.raises(TypeError):
        bubble_sort(input_string)