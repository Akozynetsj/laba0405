#4
class BankAccount:
    def __init__(self, balance = 0, owner):
        self.balance = balance
        self.owner = owner
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'{amount}грн. успішно додано до рахунку {self.owner}')
        else:
            print('Сума поповнення має бути більша нуля')
    def withdraw(self,amount):
        if self.balance >= amount > 0:
            self.balance -= amount
            print(f'{amount}грню успішно знято з рахунку {self.owner}')
        else:
            print('Недостатньо коштів на рахунку або сума зняття має бути більше нуля')
    def get_balance(selfself):
        return self.balance


