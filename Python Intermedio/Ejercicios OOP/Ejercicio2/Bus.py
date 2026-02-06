from Person import Person

class Bus():
    
    
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers_list = []
    
    
    def pick_up_passengers(self):
        try:
            name = input("Digite el nombre del pasajero: ")
            age = int(input("Digite la edad del pasajero:"))
            
            new_passenger = Person(name, age)
            
            self.passengers_list.append(new_passenger)
            print(f"{new_passenger.name} agregado.")
            
        except ValueError:
            print("Ingrese una opción válida.")


    def request_add_passenger(self):
        while True:

            if len(self.passengers_list) >= self.max_passengers:
                print("\nLímite máximo de pasajeros alcanzado.")
                return

            self.pick_up_passengers()
            
            if not self.ask_continue_adding():
                return


    def ask_continue_adding(self):
        while True:
            
            continue_option = input("Desea seguir agregando otro pasajero (S/N)?").upper()
            
            if continue_option == 'S':
                return True
            elif continue_option == 'N':
                return False
            else:
                print("Digite una opcion valida.")


    def drop_passenger(self):
        if len(self.passengers_list) == 0:
            print("El bus se encuentra vacío.")
            return

        name_to_remove = input("Digite el nombre del pasajero a bajar: ")

        for passenger in self.passengers_list:
            if passenger.name.lower() == name_to_remove.lower():
                self.passengers_list.remove(passenger)
                print(f"{passenger.name} se ha bajado del bus.")
                return

        print(f"No se encontró ningún pasajero llamado '{name_to_remove}'.")


    def show_passengers(self):
        print("\nPasajeros en el bus:")

        if not self.passengers_list:
            print("El bus está vacío.")
        else:
            for p in self.passengers_list:
                print(f"- {p.name}, {p.age} años")
