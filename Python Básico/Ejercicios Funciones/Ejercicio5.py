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