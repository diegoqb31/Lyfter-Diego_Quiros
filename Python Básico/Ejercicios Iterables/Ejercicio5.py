print("\nEjercicio 5\n")

my_list = []

for i in range(0, 10):
    number = int(input(f"{i + 1} - Ingrese un numero: "))
    my_list.append(number)
    if i == 0 or max < number:
        max = number

for x in my_list:
    print(x)

print(f"El numero mas alto fue: {max}")
