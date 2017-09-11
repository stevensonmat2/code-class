

class BankAccount:
    def __init__(self, f_name, l_name, balance):
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = self.f_name + ' ' + self.l_name
        self.balance = balance
        self.inv = []
        self.setup()

    def deposit(self, amount):
        self.balance += amount
        print('thanks {}'.format(amount, self.balance))

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print('you took {}'.format(amount))
        else:
            print('not neough $')




    def setup(self):
        print('you have to create an account for {}.'.format(self.full_name))


    def __str__(self):
        return 'account of {}.'.format(self.full_name)

    def __repr__(self):
        return self.__str__()



class altBankAccount(BankAccount):

    def withdraw(self, amount, cancel=False):
        if cancel:
            return super().withdraw(amount)

        elif self.balance - amount - 200 >= 0:
            self.balance -= amount
            print('you took {}'.format(amount))
        else:
         print('insufficient funds')



account1 = BankAccount('chris', 'jones', 60)
account2 = altBankAccount('else', 'hat', 5000)


print(account1.balance)
print(account2.balance)
account2.withdraw(5000, True)
print(account2.balance)