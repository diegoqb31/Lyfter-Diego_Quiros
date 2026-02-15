# print_numbers_times_2
def print_numbers_times_2(numbers_list):
	for number in numbers_list: # O(n) porque corre n veces (tamaño de la lista)
		print(number * 2) # O(1)

#El tiempo de complejidad es O(n) ya que hay un único ciclo que se ejecuta n veces



#check_if_lists_have_an_equal
def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a: # O(n) porque corre n veces (tamaño de la lista a)
		for element_b in list_b: # O(m) porque corre m veces (tamaño de la lista b) -> O(n*m)
			if element_a == element_b: # O(1)
				return True # O(1)
				
	return False # O(1)

#El tiempo de ejecución es O(n*m) ya que se tienen dos cliclos anidados con posibilidad de diferente tamaño de listas



#print_10_or_less_elements
def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print) # O(1) 
	for index in range(min(list_len, 10)): #O(1) porque se ejecuta máximo 10 veces
		print(list_to_print[index]) # O(1)

#El tiempo de complejidad es O(1)



#generate_list_trios
def generate_list_trios(list_a, list_b, list_c):
	result_list = []
	for element_a in list_a: #O(n) porque corre n veces (tamaño de la lista a)
		for element_b in list_b: #O(m) porque corre m veces (tamaño de la lista b) -> O(n*m)
			for element_c in list_c: #O(p) porque corre p veces (tamaño de la lista c) -> O(n*m*p)
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 

#El tiempo de ejecución es O(n*m*p) ya que se tienen tres cliclos anidados con posibilidad de tres diferentes tamaños de lista