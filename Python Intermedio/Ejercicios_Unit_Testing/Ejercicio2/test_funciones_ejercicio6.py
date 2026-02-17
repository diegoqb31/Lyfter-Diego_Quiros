from Ejercicios_Funciones import sort_list, order_string, join_list
import pytest

#order_string
def test_order_string_with_few_values():
    assert order_string("banana-apple-orange") == ["banana", "apple", "orange"]


def test_order_string_with_number_parameter():
    input_number = 12334
    with pytest.raises(TypeError):
        order_string(input_number)


def test_order_string_with_one_value():
    assert order_string("banana") == ["banana"]


#sort_list
def test_sort_list_with_number_parameter():
    input_number = 12334
    with pytest.raises(TypeError):
        sort_list(input_number)


def test_sort_list_already_sorted():
    test_list = ["apple", "banana", "orange"]
    sort_list(test_list)
    assert test_list == ["apple", "banana", "orange"]


def test_sort_list_with_duplicates():
    data = ["apple", "banana", "apple"]
    sort_list(data)
    assert data == ["apple", "apple", "banana"]

#join_list
def test_join_list_big_string():
    test_list = [
        "Python123",
        "DataStructures456",
        "Algorithms789",
        "Testing000"
    ]

    expected = "Python123-DataStructures456-Algorithms789-Testing000"
    assert join_list(test_list) == expected


def test_join_list_empty_list():
    test_list = []
    assert join_list(test_list) == ""


def test_join_list_elements_with_hyphens():
    test_list = ["pre-existing", "data-set", "test-case"]

    expected = "pre-existing-data-set-test-case"
    assert join_list(test_list) == expected



