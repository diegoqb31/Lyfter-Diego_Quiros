from BankAccount import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance)
        self.min_balance = min_balance

    def get_money(self, quantity):
        if quantity <= 0:
            print("El monto tiene que ser superior a cero.")
        elif (self.balance - quantity) < self.min_balance:
             raise ValueError("El monto minimo no permite esta transacción.")
        else:
            self.balance -= quantity
            print(f"Se rebajan {quantity}, Nuevo balance: {self.balance}")