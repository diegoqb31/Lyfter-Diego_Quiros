print("Ejercicio #1\n")


print("Hola" + "Mundo") #HolaMundo
#print("Diego" + 26) #TypeError: can only concatenate str (not "int") to str
#print(41 + "Lyfter") #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print([1,2,3], [4,5,6]) #[1, 2, 3] [4, 5, 6]
#print("Arreglo" + [7,7,7]) #TypeError: can only concatenate str (not "list") to str
print(1.7 + 2) #3.7
print(True + False) #1



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


print("\nEjercicio #5\n")


grade_counter = 1
number_of_approved_notes = 0
number_of_disapproved_notes = 0
sum_of_approved_items = 0
sum_of_disapproved_items = 0
total_sum = 0

total_number_of_grades = int(input("Digite la cantidad de notas: "))

while grade_counter <= total_number_of_grades:
    print(f"Ingrese la nota número {grade_counter}: ")
    current_note = float(input())
    
    if current_note < 70:
        number_of_disapproved_notes += 1
        sum_of_disapproved_items += current_note
    else:
        number_of_approved_notes += 1
        sum_of_approved_items += current_note
        
    total_sum += current_note
    grade_counter += 1

if number_of_approved_notes > 0:
    average_of_approved_grades = sum_of_approved_items / number_of_approved_notes
else:
    average_of_approved_grades = 0

if number_of_disapproved_notes > 0:
    average_of_disapproved_grades = sum_of_disapproved_items / number_of_disapproved_notes
else:
    average_of_disapproved_grades = 0

average_of_total_grades = total_sum / total_number_of_grades


print(f"El estudiante tiene esta cantidad de notas aprobadas: {number_of_approved_notes}")
print(f"Este es el promedio de notas aprobadas: {average_of_approved_grades}")
print(f"El estudiante tiene esta cantidad de notas desaprobadas: {number_of_disapproved_notes}")
print(f"Este es el promedio de notas desaprobadas: {average_of_disapproved_grades}")
print(f"Este es el promedio total de notas: {average_of_total_grades}")