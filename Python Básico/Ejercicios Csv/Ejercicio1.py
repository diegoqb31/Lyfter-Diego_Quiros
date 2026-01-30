import csv

def add_videogames(videogames_list):
    
    name = input("Digite el nombre: ")
    genre = input("Digite el género: ")
    developer = input("Digite el desarrollador: ")
    esrb_rating =  input("Digite la calificación ESRB: ")
    
    if not all([name, genre, developer, esrb_rating]):
        print("Hay campos en blanco. No se agregó el videojuego.")
        return False
        
    new_game = {"name": name, "genre": genre, "developer": developer, "esrb_rating": esrb_rating}
    
    videogames_list.append(new_game)
    print("Videojuego agregado correctamente.")
    
    return True


def ask_continue_adding():
    while(True):
        option = input("Desea agregar otro videojuego (S\\N):").strip().upper()
            
        if option == 'S':
            return True
        elif option == 'N':
            return False
        else:
            print("*****Digite una opción válida*****")


def write_csv_file(file_path, data, headers, dialect):
    
    try:
        with open(file_path, 'w', newline = '', encoding='utf-8') as file:
            writer = csv.DictWriter(file, headers, dialect=dialect)
            writer.writeheader()
            writer.writerows(data)
    except IOError as error:
        print(f"Error al escribir el archivo: {error}")


def process_videogames(file, dialect):
    videogames_list = []
    try:
        while(True):
            
            added = add_videogames(videogames_list)
            if added:
                if not ask_continue_adding():
                    break
            else:
                option = input("¿Desea intentar nuevamente? (S/N): ").strip().upper()
                if option != 'S':
                    break
        
        if len(videogames_list) == 0: 
            print("La lista está vacía, no se genera el archivo.") 
            return
        
        videogames_headers = videogames_list[0].keys()
        write_csv_file(file, videogames_list, videogames_headers, dialect)
    
    except Exception as error:
        print(f"Ha ocurrido un error: {error}")


def main():
    print("\n Ejercicio #1\n")
    process_videogames('videogames.csv', 'excel')
    
    print("\n Ejercicio #2\n")
    process_videogames('videogames_tab.csv','excel-tab')

main()