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