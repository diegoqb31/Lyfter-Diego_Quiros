import Actions
import Menu
import Data
import Student

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
                    Actions.add_student(students_list)
                    if Actions.ask_continue_adding() == False:
                        break;
                    
            case 2:
                #Mostrar estudiantes si la lista no está vacía
                if len(students_list) == 0:
                    print("No hay estudiantes agregados.")
                    input("\nPresione Enter para continuar...")
                else:
                    Actions.show_Students(students_list)
                    input("\nPresione Enter para continuar...")
            case 3:
                #Mostrar los 3 primeros promedios, si la lista no está vacía
                if len(students_list) == 0:
                    print("No hay estudiantes agregados.")
                    input("\nPresione Enter para continuar...")
                else:
                    Actions.top3_grades(students_list)
                    input("\nPresione Enter para continuar...")
                
            case 4:
                #Mostrar todos promedios, si la lista no está vacía
                if len(students_list) == 0:
                    print("No hay estudiantes agregados.")
                    input("Presione Enter para continuar...")
                else:
                    print(f"Promedio del total de alumnos: {Actions.calculate_total_averages(students_list)}\n")
                    input("\nPresione Enter para continuar...")
                
            case 5:
                #Si hay datos para guardar, se guarda sobreescribiendo si no existe un archivo o está vacío, 
                # de lo contrario se pregunta de que modo se quiere guardar la información
                if len(students_list) == 0:
                    print("No hay nada por guardar aún.")
                    input("\nPresione Enter para continuar...")
                else:
                    if Data.ask_file_is_new_or_empty('students.csv'):
                        Data.save_students_overwrite('students.csv', students_list)
                        input("\nPresione Enter para continuar...")
                    else:
                        Actions.ask_save_data(students_list)
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


def Main():
    """
    Función inicial main.
    """
    start_menu()

Main()