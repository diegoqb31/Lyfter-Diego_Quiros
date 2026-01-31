print("\nEjercicio #4\n")

number1 = int(input("Digite el primer numero: "))
number2 = int(input("Digite el segundo numero: "))
number3 = int(input("Digite el tercer numero: "))

if number1 >= number2 and number1 >= number3:
    higher = number1
elif number2 >= number1 and number2 >= number3:
    higher = number2
else:
    higher = number3

print("El número mayor es:", higher)