def grades_decorator(func):
    def wrapper(*args):
        
        print("Notas a evaluar:", args)

        result_list = func(*args)

        print("Notas que aprobaron:", result_list)

        return result_list

    return wrapper


@grades_decorator
def approved_grades(*args):
        approved_list = []
        for index, arg in enumerate(args):
            if arg >= 70:
                approved_list.append(arg)
        return approved_list

def main():
    
    approved_grades(75,45,92,99,61,84,41,20)
    

main()