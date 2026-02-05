import Actions

def show_menu():
    """
    Únicamente muestra el menú.
    """
    print("\n***SISTEMA DE ESTUDIANTES***\n")
    print("1- Ingresar estudiante")
    print("2- Ver informacion de estudiantes")
    print("3- Ver el top 3 de estudiantes con la mejor nota")
    print("4- Ver la nota promedio de todos los estudiantes")
    print("5- Exportar datos actuales a un CSV")
    print("6- Importar datos actuales desde un CSV")
    print("7 - SALIR\n")


def request_menu_option():
    """
    Se encarga de pedir una opción válida al usuario.

    Parámetros:
        No recibe parámetros.

    Retorna:
        Si la opción es válida la retorna.
    """
    try:
        menu_option = int(input("Digite la operacion a realizar: "))
            
        if menu_option < 1 or menu_option > 7:
            raise ValueError()
            
        return menu_option
            
    except ValueError:
        print("Ingrese una opción válida.")


def request_save_menu_option():
    """
    Se encarga de preguntar al usuario como desea el guardado de la información.

    Parámetros:
        No recibe parámetros.

    Retorna:
        Si la opción es válida la retorna.
    """
    try:
        save_mode_option = int(input("\nComo desea guardar el contenido?\n1- Sobreescribir el contenido actual\n2- Agregar mas contenido al archivo actual\n3- Salir\n Opcion:"))
            
        if save_mode_option < 1 or save_mode_option > 3:
            raise ValueError()
            
        return save_mode_option
            
    except ValueError:
        print("Ingrese una opción válida.")
