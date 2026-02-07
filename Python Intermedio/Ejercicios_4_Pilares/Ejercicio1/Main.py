from SavingsAccount import SavingsAccount

def Main():
    bank_account = SavingsAccount(100, 20)
    print(f"Se creó la cuenta con un mínimo de {bank_account.min_balance} y un balance de {bank_account.balance}")
    bank_account.get_money(20)
    bank_account.deposit_money(40)
    bank_account.get_money(70)
    bank_account.get_money(70)
    bank_account.get_money(40)
Main()


