
"""class name should start with uppercase"""
# class Animal:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#
#     def display(self):
#         print(f"Animal:{self.name}  price:{self.price}")
#
# # Creating an object
# cow_animal=Animal("cow",100000)
# cow_animal.display()


# class BankAccount:
#     def __init__(self,account_number,balance):
#         self.account_number=account_number
#         self.__balance=balance
#
#     # getter method to access balance (Read-only)
#     def get_balance(self):
#         return self.__balance
#
#     # setter method to update balance(Restricted Modification)
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance +=amount
#             print(f"{amount} deposited successfully")
#         else:
#             print("invalid deposit amount!")
#
#     def withdraw(self,amount):
#         if 0 < amount <=self.__balance:
#             self.__balance-=amount
#             print(f"{amount} withdraw successfully")
#         else:
#             print("Insufficient balance or invalid amount! ")
#
#     def display_account(self):
#         print(f"Account Number:{self.account_number}, Balance:{self.__balance}")
#
#
# account=BankAccount("1234567890", 5000)
#
# print("Initial balance:",account.get_balance())
#
# account.deposit(2000)
#
# account.withdraw(3000)
#
# account.display_account()