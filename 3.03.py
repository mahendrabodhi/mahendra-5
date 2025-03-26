"""for loop """

# name="mahendra"
# password="ma123"
#
# username=input("enter username: ")
# password_=input("enter password: ")
#
# if username==name and password_==password:
#     print("login successful")
#
# else:
#     print("invalid credentials")



# import threading
# import time
#
# def print_numbers():
#     for i in range(1, 6):
#         time.sleep(1)
#         print(f"Number: {i}")
#
# def print_letters():
#     for letter in 'ABCDE':
#         time.sleep(1)
#         print(f"Letter: {letter}")
#
# # Creating threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
#
# # Starting threads
# thread1.start()
# thread2.start()
#
# # Waiting for both threads to finish
# thread1.join()
# thread2.join()
#
# print("Finished all threads!")

import pickle

# Data to be pickled
# dataa = {"name": "Yaswanth", "age": 30, "skills": ["Python", "SQL", "AWS"]}
#
# # 🔹 Pickling: Saving object to file
# with open("dataa.pkl", "wb") as file:
#     pickle.dump(dataa, file)
#
# print("✅ Data Pickled and Saved Successfully")

# 🔹 Unpickling: Loading object from file
# with open("data.pkl", "rb") as file:
#     loaded_data = pickle.load(file)
#
# print("✅ Unpickled Data:", loaded_data)



# import pickle
#
# # Unpickling an object from a file
# with open("data.pkl", "rb") as file:
#     data = pickle.load(file)
#
# print("Unpickled Data:", data)


"""MRO -"""

# class A:
#     def show(self):
#         print("Class A")
#
# class B(A):
#     def show(self):
#         print("Class B")
#         super().show()  # Calls method from A
#
# class C(A):
#     def show(self):
#         print("Class C")
#         super().show()  # Calls method from A
#
# class D(B, C):  # Multiple Inheritance
#     def show(self):
#         print("Class D")
#         super().show()  # Calls method from B, then follows MRO
#
# # Creating an instance of D
# d = D()
# d.show()
#
# # Checking MRO
# print(D.mro())  # OR print(D.__mro__)

#
# class Employee:
#     company="TechCorp"
#
#     @classmethod
#     def set_compnay(cls,new_name):
#         cls.company=new_name
#
#     @classmethod
#     def get_company(cls):
#         return cls.company
#
# print(Employee.get_company())
#
# Employee.set_compnay("QuickTech")
# print(Employee.get_company())


# class Employee:
#     company="Techcorp"
#
# print(Employee.company)
#
# Employee.company="QuickCorp"
# print(Employee.company)

# class Employee:
#     company="TechCorp"
#
#     @classmethod
#     def set_company(cls,new_name):
#         cls.company=new_name
#
#     @classmethod
#     def get_company(cls):
#         return cls.company
#
# print(Employee.get_company())
#
# Employee.company="QuickCorp"
# print(Employee.get_company())



print("Hello, GitHub! I made changes.")
print("Hello, GitHub! I made changes.")
print("To clone a repository, use the following command:")
print("git clone <repository_URL>")
print("This creates a local copy of the project from GitHub.")
