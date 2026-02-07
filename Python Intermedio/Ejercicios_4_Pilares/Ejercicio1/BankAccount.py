class BankAccount:
    
    def __init__(self, balance):
        self.balance = balance


    def deposit_money(self, quantity):
        if quantity <= 0:
            print("El monto tiene que ser superior a cero.")
        else:
            self.balance += quantity
            print(f"Se depositan {quantity}, Nuevo balance: {self.balance}")
    
    
    def get_money(self, quantity):
        if quantity <= 0:
            print("El monto tiene que ser superior a cero.")
        elif (self.balance - quantity) < self.balance:
            print("No se cuenta con fondos suficienctes.")
        else:
            self.balance -= quantity
            print(f"Se rebajan {quantity}, Nuevo balance: {self.balance}")