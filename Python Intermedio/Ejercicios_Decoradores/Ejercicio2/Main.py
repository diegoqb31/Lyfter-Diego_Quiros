def validate_numbers_decorator(func):
    def wrapper(*args):
        
        for index, arg in enumerate(args):
            if not (isinstance(arg, (int, float, complex))):
                raise ValueError(f"El elemento {arg} no es de tipo number")
        
        return func(*args)
        
    return wrapper


@validate_numbers_decorator
def approved_grades(*args):
        approved_list = []
        for index, arg in enumerate(args):
            if arg >= 70:
                approved_list.append(arg)
        return approved_list

def main():
    
    approved_grades_list = approved_grades(75,45,92,99,61,84,41,20)
    print(f"Notas aprobadas:{approved_grades_list}")

    approved_grades_list_2 = approved_grades(75,45,92,'85',61,84,41,20)
    print(f"Notas aprobadas:{approved_grades_list_2}")
    
main()