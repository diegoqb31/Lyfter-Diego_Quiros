print("\nEjercicio #6\n")


def order_string(test_string):
    order_words = []
    word = ""
    for letter in test_string:
        if letter != "-":
           word += letter
        else:
            order_words.append(word)
            word = ""
    
    order_words.append(word)
    return order_words


def sort_list(order_words):
    n = len(order_words)

    for i in range(n):
        for j in range(n - 1):
            if order_words[j] > order_words[j + 1]:
                order_words[j], order_words[j + 1] = order_words[j + 1], order_words[j]

        
def join_list(order_list):
    result_string = ""
    for i in range(len(order_list)):
        result_string += order_list[i]
        if i < len(order_list) - 1:
            result_string += "-"

    return result_string


order_words = order_string("python-variable-funcion-computadora-monitor")
sort_list(order_words)
print(join_list(order_words))