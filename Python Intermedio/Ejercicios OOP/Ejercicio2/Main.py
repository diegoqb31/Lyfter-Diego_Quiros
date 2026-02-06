from Bus import Bus

def main():

    bus = Bus(4)

    while True:
        print("\n===== GESTIONAR BUS =====")
        print("1. Agregar pasajeros")
        print("2. Bajar pasajero")
        print("3. Ver pasajeros")
        print("4. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            bus.request_add_passenger()

        elif option == "2":
            bus.drop_passenger()

        elif option == "3":
            bus.show_passengers()

        elif option == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
