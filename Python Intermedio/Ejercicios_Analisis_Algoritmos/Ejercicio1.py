def bubble_sort(new_list):
    
    for _ in new_list: # O(n) porque corre n veces (tamaño de la lista)
        for i in range(0, len(new_list) - 1): # O(n) porque corre n veces (tamaño de la lista)
            if(new_list[i] > new_list[i+1]): # O(1)
                new_list[i], new_list[i+1]  = new_list[i+1], new_list[i] #O(1)
    print(new_list) #O(1)
    
    #El tiempo de ejecución es O(n^2) ya que se tienen dos cliclos anidados 