print("\nEjercicio 1\n")

first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la","por", "es", "util"]

for i in range(0, len(first_list)):
    print(first_list[i] + " " + second_list[i])


print("\nEjercicio 2\n")

my_string = "Pizza con piña"

for i in range(len(my_string) -1, -1, -1):
    print(my_string[i])
    

print("\nEjercicio 3\n")

my_list = [4, 3, 6, 1, 7]

my_list[0], my_list[-1] = my_list[-1], my_list[0]

for i in my_list:
    print(i)


print("\nEjercicio 4\n")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

final_list = []

for i in range(0, len(my_list)):
    if(my_list[i] % 2) == 0:
        final_list.append(my_list[i])

for j in final_list:
    print(j)

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
