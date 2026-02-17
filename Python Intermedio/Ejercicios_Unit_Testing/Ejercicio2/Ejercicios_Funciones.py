#Ejercicio 3

def sum_all_elements_of_list(list_of_numbers):
    sum_result = 0
    for number in list_of_numbers:
        sum_result += number
    return sum_result

#Ejercicio 4

def reverse_string(test_string):
    result_string = ""
    for i in range(len(test_string) -1, -1, -1):
        result_string += test_string[i]
    return result_string

#Ejercicio 5

def count_uppercase_lowercase(test_string):
    quiantity_upper_cases, quiantity_lower_cases = 0, 0
    for letra in test_string:
        if letra.isupper():
            quiantity_upper_cases += 1
        elif letra.islower():
            quiantity_lower_cases += 1

    return quiantity_upper_cases, quiantity_lower_cases

#Ejercicio 6

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
    
    return order_words

        
def join_list(order_list):
    result_string = ""
    for i in range(len(order_list)):
        result_string += order_list[i]
        if i < len(order_list) - 1:
            result_string += "-"

    return result_string

#Ejercicio 7

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