print("\nEjercicio 4\n")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

final_list = []

for i in range(0, len(my_list)):
    if(my_list[i] % 2) == 0:
        final_list.append(my_list[i])

for j in final_list:
    print(j)