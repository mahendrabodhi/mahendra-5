
"""class"""

"""single inheritance"""
# class Animal:
#     def animal_details(self):
#         print("animal is cow")
#
# class Forest(Animal):
#     def forest_details(self):
#         print("forest is animal forest")
#
# object=Forest()
#
# object.animal_details()


"""method overriding"""
# class Animal:
#     def animal_details(self):
#         print("animal is cow")
#
# class Forest(Animal):
#     def animal_details(self):
#         print("Animal in the forest is Tiger")
#
# object=Forest()
#
# object.animal_details()


"""method overloading"""

# class Example:
#     def show(self,a):
#         print("Ono arguments:",a)
#
#     def show(self,a,b):
#         print("Two arguments:",a,b)
#
# object=Example()
# object.show(10,20)


# class Test:
#     def display(self,a):
#         print("One argument:",a)
#
#     def display(self,a,b):
#         print("Two arguments:",a,b)
#
# object=Test()
#
# object.display(10,20)


# class Test:
#     def display(self,*args):
#         print("Arguments:",args)
#
# obj=Test()
#
# obj.display()
# obj.display(10)
# obj.display(10,20)
# obj.display(10,20,30)

"""using default arguments"""


# class  Calculator:
#     def add(self,a=0,b=0,c=0):
#         return a+b+c
#
# obj=Calculator()
#
# print(obj.add())
# print(obj.add(5))
# print(obj.add(5,5))
# print(obj.add(5,10,15))    ## 30 (Three arguments)



