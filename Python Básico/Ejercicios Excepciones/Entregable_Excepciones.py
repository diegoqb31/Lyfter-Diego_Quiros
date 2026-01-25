def init_menu():
    option = 0
    current_number = 0
    while(option != 6):
        option = show_menu(current_number)
        match option:
            case 1:
                current_number = add(current_number)
            case 2:
                current_number = subtract(current_number)
            case 3:
                current_number = multiply(current_number)
            case 4:
                current_number = divide(current_number)
            case 5:
                current_number = 0
            case 6:
                print("SALIENDO")
    

def show_menu(current_number):
    while True:
        print("\n*******CALCULADORA*******\n")
        print(f"Numero actual: {current_number}")
        print("1 - Suma")
        print("2 - Resta")
        print("3 - Multiplicacion")
        print("4 - División")
        print("5 - Borrar Resultado")
        print("6 - Salir")
        
        try:
            option = int(input("Digite la operacion a realizar: "))
            
            if option < 1 or option > 6:
                raise ValueError()
            
            return option
            
        except ValueError:
            print("Ingrese una opción válida")


def add(current_number):
    try:
        number = float(input(f"Digite el número a sumarle a {current_number}: "))
        return current_number + number
    except ValueError as ex:
        print("Ingrese un número válido")
        return add(current_number)


def subtract(current_number):
    try:
        number = float(input(f"Digite el número a restarle a {current_number}: "))
        return current_number - number
    except ValueError as ex:
        print("Ingrese un número válido")
        return subtract(current_number)


def multiply(current_number):
    try:
        number = float(input(f"Digite el número a multiplicarle a {current_number}: "))
        return current_number * number
    except ValueError as ex:
        print("Ingrese un número válido")
        return multiply(current_number)


def divide(current_number):
    try:
        number = float(input(f"Digite el número a dividirle a {current_number}: "))
        if number == 0:
            raise ZeroDivisionError
        return current_number / number
    except ValueError:
        print("Ingrese un número válido")
        return divide(current_number)
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return divide(current_number)


init_menu()