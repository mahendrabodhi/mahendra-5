"""for loop"""

# for i in range(10):
#     print(i,end=" ")


"""functions with args"""
# def add(*args):
#     return sum(args)
#
# result=add(5,6,7)
# print(result)


# def add(*args):
#     print(sum(args))
#
# add(10,10)

"""join arguments"""
# def join_strings(*args):
#     return " ".join(args)
# join_args=join_strings("hello","world")
# print(join_args)

"""find maximum value"""

# def max_value(*args):
#     return max(args)
# result=max_value(1,10,100,1000)
# print(result)

"""printing all arguments"""

# def print_values(*args):
#     for arg in args:
#         print(arg,end=" ")
# print_values(10,"hello","hai",1000)


"""multiply of all arguments"""
# def multiply_all(*args):
#     result=1
#     for number in args:
#         result*=number
#     return result
#
# print(multiply_all(1,2,3,4,5))

"""defining and callings"""
# def greet():
#     print("hello,welcome to python!")
# greet()

"""function with parameters"""
# def add_numbers(a,b):
#     return a+b
# result=add_numbers(5,10)
# print(result)

"""function with default parameters"""
# def greet(name="Guest"):
#     print(f"Hello,{name}")
#
# greet("Manikanta")
# greet()


"""function with return statement"""
# def square(num):
#     return num*num
#
# result=square(4)
# print(result)

"""function with multiple return values"""

# def calculate(a,b):
#     sum_=a+b
#     diff_=a-b
#     mul_=a*b
#     return sum_,diff_,mul_
# x,y,z=calculate(10,5)
# print(f"sum:{x}, difference:{y}, multiply:{z}")


"""lambda functions"""

# square=lambda x:x*x
# print(square(5))
#
#
# square=lambda x,y:x*y
# print(square(5,7))


"""recursion functions"""

# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(7))


"""function with arbitrary arguments"""

# def add_all(*numbers):
#     return sum(numbers)
# print(add_all(1,10,100,1000,10000))

"""**kwargs (multiple keyword arguments)"""

# def student_info(**details):
#     for key,value in details.items():
#         print(f"{key}:{value}")
#
# student_info(name="mahendra",age=25,course="python")


"""nested functions(functions inside another function)"""

# def outer():
#     print("outer function")
#
#     def inner():
#         print("inner function")
#
#     inner()
#
# outer()


"""function with global and local variables"""

# x=10
# def modify():
#     global x
#     x=x+5
#     print("inside function:",x)
#
# modify()
# print("outside function:",x)