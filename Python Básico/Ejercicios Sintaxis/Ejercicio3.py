print("\nEjercicio #3\n")


import random

random_number = random.randint(1, 10)

user_number = 0

while(user_number != random_number):
    user_number = int(input("Ingrese un numero entre el 1 y el 10: "))
    if(user_number < 1 or user_number > 10):
        print("Digite un numero valido entre 1 y 10")
    elif (user_number != random_number):
            print("Intentelo de nuevo ")

print("Acertaste el numero")