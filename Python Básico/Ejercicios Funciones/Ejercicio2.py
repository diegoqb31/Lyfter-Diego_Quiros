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