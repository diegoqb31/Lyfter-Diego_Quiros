from Ejercicios_Funciones import sum_all_elements_of_list

def test_sum_all_elements_positive_numbers():
    assert sum_all_elements_of_list([1, 2, 3, 4]) == 10


def test_sum_all_elements_with_negatives():
    assert sum_all_elements_of_list([-1, 5, -3]) == 1


def test_sum_all_elements_without_value():
    assert sum_all_elements_of_list([]) == 0
