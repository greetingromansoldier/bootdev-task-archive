# code before changes:

# class BankAccount:
#     def __init__(self, account_number, initial_balance):
#         pass

#     def get_account_number(self):
#         pass

#     def get_balance(self):
#         pass

#     def deposit(self, amount):
#         pass

#     def withdraw(self, amount):
#         pass

# actual code:

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError ("cannot deposit zero or negative funds")

        self.__balance += amount


    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError ("cannot withdraw zero or negative funds")
        if self.__balance < amount:
            raise ValueError ("insufficient funds")

        self.__balance -= amount
