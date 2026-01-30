print("Ejercicio #2\n")


list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

person = {}

if(len(list_a) == len(list_b)):
    for i in range(0, len(list_a)):
        person[list_a[i]] = list_b[i]

for column, data in person.items():
    print(f'{column} : {data}')