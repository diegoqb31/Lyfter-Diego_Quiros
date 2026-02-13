def bubble_sort(new_list):
    
    for _ in new_list:
        for i in range(0, len(new_list) - 1):
            if(new_list[i] > new_list[i+1]):
                new_list[i], new_list[i+1]  = new_list[i+1], new_list[i]
    print(new_list)


def reverse_bubble_sort(new_list):
    
    for _ in new_list:
        for i in range(len(new_list)-1, 0,-1):
            if(new_list[i] < new_list[i-1]):
                new_list[i], new_list[i-1]  = new_list[i-1], new_list[i]
    print(new_list)

new_list = [8,5,3,1,4,7,9]

new_list_2 = [8,5,3,1,4,7,9]

bubble_sort(new_list)
reverse_bubble_sort(new_list_2)
