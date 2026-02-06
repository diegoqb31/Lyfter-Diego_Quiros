from Student import Student
import csv
import os

def ask_file_is_new_or_empty(file_path):
    """
    Verifica si un archivo no existe o existe pero está vacío.

    Parámetros:
        file_path (str): Ruta del archivo a verificar.

    Retorna:
        bool: True si el archivo no existe o está vacío, False si ya tiene contenido.
    """
    if not os.path.exists(file_path):
        return True

    if os.path.getsize(file_path) == 0:
        return True

    return False


def save_students_append(file_path, new_students_list):
    """
    Sobreescribe únicamente los registros de estudiantes que no estaban cargados previamente.

    Parámetros:
        file_path (str): Ruta del archivo a verificar.
        new_student_list (list): Lista de estudiantes nuevos.

    Retorna:
        La función no retorna nada.
    """
    fields = ["name", "last_name", "group", "spanish", "english", "social", "science", "average"]

    write_header = ask_file_is_new_or_empty(file_path)

    with open(file_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        
        if write_header:
            writer.writeheader()

        for student in new_students_list:
            writer.writerow({
                "name": student.name,
                "last_name": student.last_name,
                "group": student.group,
                "spanish": student.spanish,
                "english": student.english,
                "social": student.social,
                "science": student.science,
                "average": student.average
            })
    print(f"{len(new_students_list)} Nuevos estudiantes agregados al archivo CSV.")


def save_students_overwrite(file_path, student_list, ):
    """
    Guarda los archivos sobreescribiendo todo.

    Parámetros:
        file_path (str): Ruta del archivo a verificar.
        student_list (list): Lista de estudiantes a guardar.
        headers (list): Lista de headers de la lista de estudiantes a guardar.

    Retorna:
        La función no retorna nada.
    """
    headers = list(student_list[0].__dict__.keys())
    try:
        with open(file_path, 'w', newline = '', encoding='utf-8') as file:
            writer = csv.DictWriter(file, headers, dialect='excel')
            writer.writeheader()
            for s in student_list:
                writer.writerow(s.__dict__)
        print(f"{len(student_list)} Nuevos estudiantes agregados al archivo CSV.")
    except IOError as error:
        print(f"Error al escribir el archivo: {error}")
        

def load_students(file_path):
    """
    Carga los registros de estudiantes guardados en el archivo CSV.

    Parámetros:
        file_path (str): Ruta del archivo a verificar.

    Retorna:
        Retorna la lista de estudiantes encontrados en el archivo CSV.
    """
    student_list = []
    
    if not os.path.exists(file_path):
        return student_list
    
    try:
        with open(file_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                student = Student(row['name'],row['last_name'],row['group'],float(row['spanish']),float(row['english']),float(row['social']), float(row['science']), float(row['average']))
                student_list.append(student)
        
        return student_list
    
    except IOError as error:
        print(f"Error al leer el archivo: {error}")
