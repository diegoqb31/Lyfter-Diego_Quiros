print("\nEjercicio #3\n")


def sum_all_elements_of_list(list_of_numbers):
    sum_result = 0
    for number in list_of_numbers:
        sum_result += number
    return sum_result


test_list = [4, 6, 2, 29] 
print(sum_all_elements_of_list(test_list))