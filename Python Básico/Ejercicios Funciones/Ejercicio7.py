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