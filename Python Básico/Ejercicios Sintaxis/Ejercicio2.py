print("\nEjercicio #2\n")


name = input("Digite su nombre: ")
last_name = input("Digite su apellido: ")
age = int(input("Digite su edad: "))

if age < 2 :
    print("Es un bebe")
elif age < 10:
    print("Es un nino")
elif age < 12:
    print("Es un preadolescente")
elif age < 18:
    print("Es un adolescente")
elif age < 29:
    print("Es un adulto joven")
elif age < 59:
    print("Es un adulto")
else:
    print("Es un adulto mayor")