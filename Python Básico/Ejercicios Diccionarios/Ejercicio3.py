print("\nEjercicio #3\n")


list_of_keys = ["access_level", "age", "hola"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}

for key in list_of_keys:
    if key in employee:
        employee.pop(key)

for column, data in employee.items():
    print(f'{column} : {data}')