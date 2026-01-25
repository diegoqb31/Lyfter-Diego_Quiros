print("Ejercicio #1\n")

hotel = {
    "name" : "Hard Rock",
    "number_of_stars": 5,
    "rooms" : [
        {"number": 7, "floor": 1, "price_per_night": 35},
        {"number": 1, "floor": 2, "price_per_night": 40},
        {"number": 30, "floor": 3, "price_per_night": 50} 
    ]
}

print("Ejercicio #2\n")


list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

person = {}

if(len(list_a) == len(list_b)):
    for i in range(0, len(list_a)):
        person[list_a[i]] = list_b[i]

for column, data in person.items():
    print(f'{column} : {data}')


print("\nEjercicio #3\n")


list_of_keys = ["access_level", "age", "hola"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}

for key in list_of_keys:
    if key in employee:
        employee.pop(key)

for column, data in employee.items():
    print(f'{column} : {data}')