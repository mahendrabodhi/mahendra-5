""""""

"""set methods """
# saving_customers = {"swamy", "teja", "raju", "ramya", "mahendra"}
# loan_customers = {'mahendra', "raju", "shiva", "dora"}
#
# common_customers = saving_customers.intersection(loan_customers)
# print(common_customers)

"""difference"""
# hr_employees = {"Alice", "Bob", "Charlie"}
# engineering_employees = {"Charlie", "David", "Eve"}
# only_hr = hr_employees.difference(engineering_employees)
# print(only_hr)

"""union --- combines without duplicates"""
# web_contacts = {"rama", "sita", "krishna"}
# app_contacts = {"krishna", "Arjun", "Bheem"}
#
# all_contacts = web_contacts.union(app_contacts)
# print(all_contacts)

"""& method, intersection"""
# python_students = {"Amit", "Sunil", "Priya", "Neha"}
# Java_students = {"Priya", "Neha", "Raj", "Rohan"}
#
# both_courses = python_students & Java_students  # same as intersection()
# print(both_courses)

"""difference_update"""

# active_products = {"P001", "P002", "P003", "P004"}
# expired_products = {"P002", "P004"}
# active_products.difference_update(expired_products)
# print(active_products)


"""find employees only in 2024"""

# employees_2023 = {"Anil", "Suresh", "Kiran"}
# employees_2024 = {"Kiran", "Ramesh", "Sunita"}
# new_hires = employees_2024 - employees_2023
# print(new_hires)

"""functions"""


# def enrolled_in_both(course1, course2):
#     return course1 & course2
#
#
# python_students = {"Amit", "Sunil", "Priya", "Neha"}
# java_students = {"Priya", "Neha", "Raj", "Rohan"}
# print(enrolled_in_both(python_students, java_students))


# def outer():
#     def inner():
#         return "Inner Function"
#     return inner()
#
# print(outer())

"""function with arguments"""
# def add(a, b):
#     return a + b
#
#
# print(add(5,10))

"""function with default arguments"""

# def greet(name="manikanta"):
#     return f"hello,{name}!"
#
#
# print(greet())
# print(greet("mahendra"))

"""function with variable length arguments"""

# def sum_elements(*numbers):
#     return sum(numbers)
#
#
# print(sum_elements(5, 6, 7))


"""using **kwargs"""

# def person_details(**details):
#     return details
#
#
# print(person_details(name= "mahendra", age= 25, city= "Hyderabad"))

"""generate functions"""

# def generate_numbers():
#     for i in range(1, 5):
#         yield i
#
#
# gen = generate_numbers()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))




"""Decorator functions"""
# def generator(func):
#     def wrapper():
#         print("before function call")
#         func()
#         print("after function call")
#     return wrapper
# @generator
# def say_hello():
#     print("hello, world!")
# say_hello()

"""Multiple decorators"""
# def uppercase_decorator(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper
#
# def exclamation_decorator(func):
#     def wrapper():
#         result = func()
#         return result + "!!!"
#     return wrapper
# @uppercase_decorator
# @exclamation_decorator
# def message():
#     return "hello"
# print(message())


# def smart_division(func):
#     def wrapper(*args, **kwargs):
#         if args[1] ==0:
#             return "Error! Division by zero is not allowed"
#         return func(*args, **kwargs)
#     return wrapper
# @smart_division
# def divide(a, b):
#     return a / b
#
#
# print(divide(10, 2))
# print(divide(5, 0))

"""Class-Based Decorators"""
# class DecoratorClass:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("Before function execution")
#         result = self.func(*args, **kwargs)
#         print("After function execution")
#         return result
#
# @DecoratorClass
# def say_hello():
#     print("Hello, Manikanta!")
# say_hello()


"""Time Measurement Decorator"""

import time

# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Execution Time:{end_time - start_time:.6f} seconds")
#         return
#     return wrapper
#
# @timer_decorator
# def long_running_task():
#     time.sleep(2)
#     print("Task completed")
#
#
# long_running_task()

"""Logging Decorator"""

# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"function '{func.__name__}' called with arguments :{args} {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @log_decorator
# def add(a, b):
#     return a + b
#
#
# print(add(3,5))

"""Access Control (Authentication) Decorator"""


# def authenticate(func):
#     def wrapper(user):
#         if user != "admin":
#             return "Access Denied!"
#         return func(user)
#     return wrapper
# @authenticate
# def dashboard(user):
#     return f"Welcome to the dashboard, {user}"

#
# print(dashboard("admin"))
# print(dashboard("guest"))






