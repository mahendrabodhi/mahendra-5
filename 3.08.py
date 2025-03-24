"""functions"""

# def greet():
#     print("hello world, welcome to python")
# greet()

# def add(a,b):
#     return a+b
#
# print("sum:",add(5,10))

"""function with parameter"""

# def add(a,b):
#     result=a+b
#     return result
#
# sum_value=add(5,10)
# print("sum:",sum_value)


"""functions with default parameters"""

# def greet(name="guest"):
#     print(f"hello,{name}")
#
# greet()
# greet("manikanta")

"""function with return statement """

# def square(num):
#     return num*num
# result=square(7)
# print(result)

"""function with multiple return values"""

# def calculate(a,b):
#     sum_value=a+b
#     mul_value=a*b
#     return sum_value,mul_value
#
# s,d=calculate(10,10)
# print("Sum:",s, "Difference:",d)


"""lambda (aAnonymous) functions"""

# square=lambda x:x*x
# print(square(5))


"""function with *args (multiple arguments)"""

# def total_sum(*numbers):
#     return sum(numbers)
#
# print(total_sum(10,20,30))

"""function with **kwargs (keyword arguments)"""

# def person_details(**details):
#     for key,value in details.items():
#         print(f"{key}:{value}")
#
# person_details(name="Manikanta",age=25,city="Miyapur")


"""Recursion function (function calling itself)"""

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# print(factorial(5))


"""basic lambda function"""

# square=lambda x:x*x
# print(square(6))

"""lambda function with multiple arguments"""

# add=lambda a,b:a+b
# print(add(5,5))

"""lambda inside a function"""

# def multiplier(n):
#     return lambda x:x*n
#
# double=multiplier(2)
# print(double(5))

"""lambda with map()"""

# numbers=[1,2,3,4,5,6,7]
# squared=list(map(lambda x:x*x,numbers))
# print(squared)

"""lambda with filter"""

# numbers=[10,15,20,25,30]
# even_numbers=list(filter(lambda x:x%2==0,numbers))
# print(even_numbers)


from functools import reduce

# numbers=[1,2,3,4,5]
# product=reduce(lambda x,y:x*y,numbers)
# print(product)

"""lambda with sorted()"""

# words=["banana","apple","cherry","blueberry"]
# sorted_words=sorted(words,key=lambda x:len(x))
# print(sorted_words)

# words=["banana","apple","cherry"]
# sorted_words=sorted(words,key=lambda x:x[-1])
# print(sorted_words)

"""lambda with if-else(ternary operator)"""

# max_num=lambda a,b:a if a>b else b
# print(max_num(10,20))


"""lambda with list comprehension"""

# numbers=[1,2,3,4,5]
# double_numbers=[(lambda x:x*2) (x) for x in numbers]
# print(double_numbers)

"""lambda with dictionary"""

# students={"alice":85,"bob":90,"charlie":80}
# sorted_students=sorted(students.items(),key=lambda x:x[0])
# print(sorted_students)

"""lambda with tuple sorting"""

# points=[(1,2),(3,1),(5,-1),(2,4)]
# sorted_points=sorted(points,key=lambda x:x[0])
# print(sorted_points)

