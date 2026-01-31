print("\nEjercicio #4\n")


def reverse_string(test_string):
    result_string = ""
    for i in range(len(test_string) -1, -1, -1):
        result_string += test_string[i]
    return result_string


my_test_string = "Hola Mundo" 
print(reverse_string(my_test_string))