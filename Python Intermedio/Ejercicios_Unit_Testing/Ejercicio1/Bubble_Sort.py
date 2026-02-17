def bubble_sort(new_list):
    if not isinstance(new_list, list):
        raise TypeError("Se debe recibir una lista como parametro")
    
    for _ in new_list:
        for i in range(0, len(new_list) - 1):
            if(new_list[i] > new_list[i+1]):
                new_list[i], new_list[i+1]  = new_list[i+1], new_list[i]
    return(new_list)


