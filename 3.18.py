
""""""


"""Library Management System (Polymorphism)"""

# class Book:
#     def details(self):
#         return "General Book Information"
#
# class ScienceBook(Book):
#     def details(self):
#         return "Science Book: Physics, Chemistry, Biology"
#
# class MathsBook(Book):
#     def details(self):
#         return "Math Book: Algebra, Geometry, Calculus"
#
# books = [ScienceBook(), MathsBook(), Book()]
#
# for book in books:
#     print(book.details())

"""ATM System (Abstraction using ABC"""

# from abc import ABC, abstractmethod
#
# class ATM(ABC):
#     @abstractmethod
#     def transaction(self):
#         pass
#
# class Withdraw(ATM):
#     def transaction(self):
#         return "Withdraw money from ATM"
#
# class Deposit(ATM):
#     def transaction(self):
#         return "Deposit money in ATM"
#
#
# w = Withdraw()
# d = Deposit()
#
# print(w.transaction())
# print(d.transaction())


"""E-Commerce Cart System"""
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Cart:
#     def __init__(self):
#         self.items = []
#
#     def add_product(self,product):
#         self.items.append(product)
#         print(f"{product.name} added to cart!")
#
#     def checkout(self):
#         total = sum(item.price for item in self.items)
#         print(f"Total Bill: {total}")
#
# p1 = Product("Laptop", 55000)
# p2 = Product("Headphones", 2000)
#
# cart = Cart()
# cart.add_product(p1)
# cart.add_product(p2)
# cart.checkout()

"""functions """
"""     *args    """


# def add_numbers(*args):
#     return sum(args)
#
#
# print(add_numbers(2, 3))
# print(add_numbers(1, 2, 3, 4, 5))

"""    **keyword arguments   """

# def print_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")
#
#
# print_info(name="Mahendra", age=25, city="Hyderabad")


"""keyword arguments"""


# def display_details(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)
#
#
# display_details(10, 20, 30, name="Rakesh", age=28)

# def greet(name, age):
#     print(f"Hello, {name}! you  are {age} years old")
#
#
# person_info = ("Mahendra", 25)
# greet(*person_info)
#
# person_details = {"name": "Rakesh", "age": 28}
# greet(**person_details)

# def log_message(level, *args, **kwargs):
#     print(f"[{level.upper()}]:", *args)
#     for key, value in kwargs.items():
#         print(f"{key} => {value}")
#
# log_message("info", "Server started", port=8080, status="Running")

