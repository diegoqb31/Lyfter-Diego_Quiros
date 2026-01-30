import json

def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
        
    except FileNotFoundError:
        print("El archivo no existe.")
        return []

    except json.JSONDecodeError:
        print("El archivo JSON está corrupto.")
        return []


def get_int_input(message):
    while True:
        try:
            value = int(input(message))
            if value < 0:
                print("El valor no puede ser negativo.")
                continue
            return value
        except ValueError:
            print("Debe ingresar un número entero válido.")


def get_non_empty_string(message):
    while True:
        value = input(message).strip()
        
        if not value:
            print("El nombre no puede estar vacío.")
            continue
        
        return value


def pokemon_exists(pokemon_list, name):
    for pokemon in pokemon_list:
        if pokemon["name"]["english"].lower() == name.lower():
            return True
    return False


def get_pokemon_types():
    types_list = []

    while True:
        pokemon_type = input("Digite el tipo del Pokémon: ").strip().capitalize()

        if not pokemon_type:
            print("El tipo no puede estar vacío, debe agaregar al menos uno.")
            continue
        
        if pokemon_type in types_list:
            print("Ese tipo ya fue agregado.")
            continue

        types_list.append(pokemon_type)

        option = input("¿Desea agregar otro tipo? (S/N): ").strip().upper()
        if option != 'S':
            break

    return types_list


def add_pokemon(pokemon_list):
    
    print("\n***Nuevo Pokemon***\n")
    
    name = get_non_empty_string("Digite el nombre: ")
    
    if pokemon_exists(pokemon_list, name):
        print("Este pokemon ya existe.")
        return
    
    types_pokemon = get_pokemon_types()
    
    hp = get_int_input("Digite el HP: ")
    attack =  get_int_input("Digite el Ataque: ")
    defense = get_int_input("Digite la defensa: ")
    sp_attack = get_int_input("Digite el Sp.Ataque: ")
    sp_defense = get_int_input("Digite el Sp.Defense: ")
    speed = get_int_input("Digite la velocidad: ")
    
        
    new_pokemon = {
    "name": {
        "english": name
    },
    "type": types_pokemon,
    "base": {
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp. Attack": sp_attack,
        "Sp. Defense": sp_defense,
        "Speed": speed
        }
    }
    
    pokemon_list.append(new_pokemon)


def ask_continue_adding():
    while(True):
        option = input("Desea agregar otro pokemon (S\\N):").strip().upper()
            
        if option == 'S':
            return True
        elif option == 'N':
            return False
        else:
            print("*****Digite una opción válida*****")


def save_pokemons(file_path, pokemons_list):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(pokemons_list, f, indent=4)
            print("Lista guardada correctamente.")
        
    except IOError as e:
        
        print(f"Error guardando el archivo: {e}")


def process_pokemons(file_path):
    pokemons_list = load_json(file_path)
    print(f"***Pokemones actuales***\n{pokemons_list}")
    try:
        while(True):
            add_pokemon(pokemons_list)
            if not ask_continue_adding():
                break
        
        save_pokemons(file_path, pokemons_list)
        
    except Exception as error:
        print(f"Ha ocurrido un error: {error}")


def main():
    process_pokemons('Pokemones.json')

main()

