print("Ejercicio #1\n")


def sum_result():
    print(sum_two_numbers())


def sum_two_numbers():
    return 5 + 5


sum_result()

print("\nEjercicio #2\n")

pi_number = 3.14


def sum_two_numbers():
    number1 = 5
    return number1 + pi_number


def multiply_two_numbers():
    number2 = 2
    global pi_number
    pi_number = 4 
    return number2 * pi_number


#print(number1) #NameError: name 'number1' is not defined 
print(sum_two_numbers()) #8.14
print(multiply_two_numbers()) #8
print(pi_number) #4

print("\nEjercicio #3\n")


def sum_all_elements_of_list(list_of_numbers):
    sum_result = 0
    for number in list_of_numbers:
        sum_result += number
    return sum_result


test_list = [4, 6, 2, 29] 
print(sum_all_elements_of_list(test_list))


print("\nEjercicio #4\n")


def reverse_string(test_string):
    result_string = ""
    for i in range(len(test_string) -1, -1, -1):
        result_string += test_string[i]
    return result_string


my_test_string = "Hola Mundo" 
print(reverse_string(my_test_string))


print("\nEjercicio #5\n")


def count_uppercase_lowercase(test_string):
    quiantity_upper_cases, quiantity_lower_cases = 0, 0
    for letra in test_string:
        if letra.isupper() == True:
            quiantity_upper_cases += 1
        elif letra.islower() == True:
            quiantity_lower_cases += 1
        
    print(f"There’s {quiantity_upper_cases} upper cases and {quiantity_lower_cases} lower cases")


count_uppercase_lowercase("I love Nación Sushi")


print("\nEjercicio #6\n")


def order_string(test_string):
    order_words = []
    word = ""
    for letter in test_string:
        if letter != "-":
           word += letter
        else:
            order_words.append(word)
            word = ""
    
    order_words.append(word)
    return order_words


def sort_list(order_words):
    n = len(order_words)

    for i in range(n):
        for j in range(n - 1):
            if order_words[j] > order_words[j + 1]:
                order_words[j], order_words[j + 1] = order_words[j + 1], order_words[j]

        
def join_list(order_list):
    result_string = ""
    for i in range(len(order_list)):
        result_string += order_list[i]
        if i < len(order_list) - 1:
            result_string += "-"

    return result_string


order_words = order_string("python-variable-funcion-computadora-monitor")
sort_list(order_words)
print(join_list(order_words))


print("\nEjercicio #7\n")


def find_prime_numbers(list_of_numbers):
    result_list = []
    for number in list_of_numbers:
        if is_prime(number):
            result_list.append(number)
    return result_list


def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    else:
        return False


print(find_prime_numbers([1,4,6,7,13,9,67]))



