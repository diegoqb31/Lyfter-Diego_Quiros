import Menu
import Data

def start_menu( ):
    """
    Inicia el programa, llama a la funcion que muestra el menú y a la que pide opción al usuario,
    guía la ejecución del programa, a través de sus 7 opciones principales.
    Función diseñada para ser llamada desde el main.

    Parámetros:
        No recibe parámetros.

    Retorna:
        La función no retorna nada.
    """
    students_list = []
    option = 0
    
    while option != 7:
        Menu.show_menu()
        option = Menu.request_menu_option()
        
        match option:
            case 1:
                #Agregar estudiante mientras el usuario así lo desee
                while True:
                    add_student(students_list)
                    if ask_continue_adding() == False:
                        break;
                    
            case 2:
                #Mostrar estudiantes si la lista no está vacía
                if len(students_list) == 0:
                    print("No hay estudiantes agregados.")
                    input("\nPresione Enter para continuar...")
                else:
                    show_Students(students_list)
                    input("\nPresione Enter para continuar...")
            case 3:
                #Mostrar los 3 primeros promedios, si la lista no está vacía
                if len(students_list) == 0:
                    print("No hay estudiantes agregados.")
                    input("\nPresione Enter para continuar...")
                else:
                    top3_grades(students_list)
                    input("\nPresione Enter para continuar...")
                
            case 4:
                #Mostrar todos promedios, si la lista no está vacía
                if len(students_list) == 0:
                    print("No hay estudiantes agregados.")
                    input("Presione Enter para continuar...")
                else:
                    calculate_total_averages(students_list)
                    input("\nPresione Enter para continuar...")
                
            case 5:
                #Si hay datos para guardar, se guarda sobreescribiendo si no existe un archivo o está vacío, 
                # de lo contrario se pregunta de que modo se quiere guardar la información
                if len(students_list) == 0:
                    print("No hay nada por guardar aún.")
                    input("\nPresione Enter para continuar...")
                else:
                    if Data.ask_file_is_new_or_empty('students.csv'):
                        students_headers = students_list[0].keys()
                        Data.save_students_overwrite('students.csv', students_list, students_headers)
                        input("\nPresione Enter para continuar...")
                    else:
                        ask_save_data(students_list)
                        input("\nPresione Enter para continuar...")

            case 6:
                #Si el archivo CSV no está vacío o existe, se cargan los estudiantes leyendo desde el CSV
                if Data.ask_file_is_new_or_empty('students.csv'):
                    print("No hay archivos ni datos que cargar\n")
                    input("\nPresione Enter para continuar...")
                else:
                    students_list = Data.load_students('students.csv')
                    print(f"Se cargaron {len(students_list)} estudiantes.")
                    input("\nPresione Enter para continuar...")
            
            case 7: 
                #Salir del programa
                print("Saliendo...")


def input_string(message):
    """
    Se encarga de pedir y validar un string al usuario.

    Parámetros:
        message (str): Mensaje para solicitar información al usuario.

    Retorna:
        Si el string es válido lo retorna.
    """
    while True:
    
        new_string = input(message)
    
        if new_string == "":
            print("El campo no puede estar vacío.")
        else:
            return new_string    


def input_float(message):
    """
    Se encarga de pedir y validar un float al usuario.

    Parámetros:
        message (str): Mensaje para solicitar información al usuario.

    Retorna:
        Si el float es válido lo retorna.
    """
    while True:
        try:
            new_float = float(input(message))
            
            if new_float < 0:
                print("El campo no puede ser menor a cero.")
                
            else:
                return new_float
            
        except ValueError:
            print("Ingrese una opción válida")


def add_student(students_list):
    """
    Se encarga de pedir la información de un nuevo estudiante, lo crea y lo agrega a la lista de estudiantes.

    Parámetros:
        students_list (list): Lista de estudiantes.

    Retorna:
        La función no retorna nada.
    """
    student_name = input_string("Digite el nombre del estudiante, sin apellidos: ")
    last_student_name = input_string("Digite los apellidos del estudiante: ")
    student_group = input_string("Digite la seccion del estudiante: ")
    spanish_grade = input_float("Digite la nota de espanol: ")
    english_grade = input_float("Digite la nota de ingles: ")
    social_grade = input_float("Digite la nota de sociales: ")
    science_grade = input_float("Digite la nota de ciencias: ")
    
    new_sudent = {'name' : student_name, 
                  'last_name': last_student_name, 
                  'group' : student_group, 
                  'spanish' : spanish_grade, 
                  'english': english_grade, 
                  'social': social_grade, 
                  'science' : science_grade}
    
    if not all([student_name, last_student_name, student_group, spanish_grade, english_grade, social_grade, science_grade]):
        print("Hay campos en blanco. No se agregó el estudiante.")
        return
    
    students_list.append(new_sudent)
    
    print(f"Estudiante {new_sudent['name']} agregado correctamente.")


def ask_continue_adding():
    """
    Se encarga de preguntar si desea seguir agregando otro estudiante.

    Parámetros:
        No recibe parámetros

    Retorna:
        True si el usuario desea agregar otro estudiante, False si no es así.
    """
    while True:
        
        continue_option = input("Desea seguir agregando otro estudiante (S/N)?").upper()
        
        if continue_option == 'S':
            return True
        elif continue_option == 'N':
            return False
        else:
            print("Digite una opcion valida.")


def ask_save_data(students_list):
    """
    Se encarga de gestionar la forma de guardado de los estudiantes, case 1 se desea sobreescribir el archivo,
    case 2 no se desea sobreescribir lo previamente guardado, si no agregar la lista actual a lo ya guardado.

    Parámetros:
        students_list (list): Lista de estudiantes.

    Retorna:
        La función no retorna nada.
    """
    students_headers = students_list[0].keys()
    save_mode_option = 0
    save_mode_option = Menu.request_save_menu_option()
    
    match save_mode_option:
        case 1:
            Data.save_students_overwrite('students.csv', students_list, students_headers)
        case 2:
            new_students_list = select_new_students_list('students.csv', students_list)
            Data.save_students_append('students.csv', new_students_list)
        case 3:
            print("Volviendo...\n")


def select_new_students_list(file_path, students_list):
    """
    Se encarga de seleccionar los estudiantes nuevos, quiere decir que se crearon, pero no se han guardado aún.

    Parámetros:
        file_path (str): Ruta del archivo donde se guardan los estudiantes.
        students_list (list): Lista de estudiantes.

    Retorna:
        Lista que contiene todos los estudiantes nuevos.
    """
    saved_students = Data.load_students(file_path)
    new_students_list = []
    
    saved_keys = {
        (student['name'], student['last_name'])
        for student in saved_students
    }
    
    for student in students_list:
        key = (student['name'], student['last_name'])
        
        if key not in saved_keys:
            
            new_students_list.append(student)
            
    return new_students_list


def show_Students(students_list):
    """
    Imprime la lista de todos los estudiantes.

    Parámetros:
        students_list (list): Lista de estudiantes.

    Retorna:
        No retorna nada, solo imprime.
    """
    if len(students_list) == 0:
        print("No hay estudiantes que mostrar.\n")
    else:
        for student in students_list:
            print(f"\nNombre: {student['name']} {student['last_name']} \nSeccion: {student['group']}\nNotas: \n\tEspanol: {student['spanish']}, \n\tIngles: {student['english']}, \n\tSociales: {student['social']}, \n\tCiencias: {student['science']}")


def calculate_average(student):
    """
    Calcula el promedio de un estudiante en específico.

    Parámetros:
        student (dict) : Estudiante del que se desea obtener su promedio.

    Retorna:
        Promedio del estudiante.
    """
    return ((student['spanish'] + student['english'] + student['social'] + student['science']) / 4)


def calculate_total_averages(students_list):
    """
    Se encarga de llamar a la funcion que calcula el promedio de cada estudiante, y muestra el promedio de todos los estudiantes, esto uno por uno.

    Parámetros:
        students_list (list): Lista de estudiantes.

    Retorna:
        La función no retorna nada.
    """
    if len(students_list) == 0:
        print("No hay estudiantes para calcular su promedio.\n")
    else:
        for student in students_list:
            print(f"\nEstudiante: {student['name']} {student['last_name']} - Seccion: {student['group']}")
            print(f"Promedio: {calculate_average(student)}")


def top3_grades(students_list):
    """
    Se encarga de llamar a la funcion que calcula el promedio de cada estudiante, y llama a la función que muestra el promedio de los estudiante,
    en este caso se le envía por parámetro los 3 mejores estudiantes.

    Parámetros:
        students_list (list): Lista de estudiantes.

    Retorna:
        La función no retorna nada.
    """
    top = []

    for student in students_list:
        avg = calculate_average(student)
        student['average'] = avg
        top.append(student)

    top.sort(key=lambda s: s['average'], reverse=True)
    top = top[:3]
    
    calculate_total_averages(top)