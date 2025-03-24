"""methods of list"""


"""append"""
# numbers=[1,2,3,4,5,6]
# numbers.append(10)
# print(numbers)

"""extend"""

# names=["hai","hello","world"]
# names.extend(["greet","define"])
# print(names)


"""insert"""

# groceries=["dal","rice","oil","veggies","greens"]
# groceries.insert(1,"pepper")
# print(groceries)


"""index"""

# fruits=["apple","orange","mango","banana"]
# fruit=fruits.index("apple")
# print(fruit)

"""remove"""
# cars=["toyota","hyundai","honda","chevrolet"]
# cars.remove("toyota")
# print(cars)

"""pop"""
# bikes=["yamaha","hero","honda"]
# last_bike=bikes.pop()
# print(last_bike)
# print(bikes)

"""count"""
# words = ["chance", "job", "coming", "chance", "success", "going", "every day"]
# count_word=words.count("chance")
# print(count_word)

"""count"""
# words = ["chance", "job", "coming", "chance", "success", "going", "every day"]
# print(words.count("chance"))

"""sort"""

# maths=["arrange","order","flow","good"]
# maths.sort()
# print(maths)

# maths=["iam", "doing", "software", "job"]
# maths.sort(key=len)
# print(maths)

# fruits = ["iam", "doing", "software", "job"]
# fruits.sort(reverse=True)
# print(fruits)

"""reverse"""
# vegetables = ["curry leaves", "tomato", "cucumber", "potato", "okra"]
# vegetables.reverse()
# print(vegetables)

"""copy"""
# series=["one", "two", "three", "four", "five"]
# series.copy()
# print(series)


"""clear"""
# numbers = [1,2,3,4,5,6,7]
# numbers.clear()
# print(numbers)

"""slicing"""

# fruits = ["apple", "mango", "banana", "orange", "grapes", "pineapple", "kiwi", "dragonfruit"]
# print(fruits[1:4])
# print(fruits[1:6])
# print(fruits[:3])
# print(fruits[2:])
# print(fruits[-4:-1])

"""list comprehension"""
# numbers = [x for x in range(1,6)]
# print(numbers)

"""list comprehension with conditions"""
# even_numbers = [x for x in range(1,15) if x % 2 == 0]
# print(even_numbers)

"""using map() with lists"""

# numbers = [1, 2, 3, 4, 5, 6]
# squared_numbers=list(map(lambda x:x**2, numbers))
# print(squared_numbers)

"""using filter() """

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers=list(filter(lambda x:x % 2 == 0, numbers))
# print(even_numbers)

"""using zip() with lists"""

# names = ["Mahendra", "Manikanta", "Rajesh"]
# age = [25, 26, 27]
# combined = list(zip(names,age))
# print(combined)


"""string methods"""

"""upper method """
# text="hello"
# print(text.upper())

"""lower methid"""
# text="HAI"
# print(text.lower())

"""capitalize"""
# text="apple"
# print(text.capitalize())

"""title"""
# text="orange is orange"
# print(text.title())

"""  strip  """
# text=" hai "
# print(text.strip())

"""l strip() ,r strip()"""
# text="  hello  "
# print(text.lstrip())
# print(text.rstrip())

"""replace()"""
# text="I love apples"
# print(text.replace("apples","mangoes"))

"""split"""
# text="apple,banana,mango"
# fruits=text.split(",")
# print(fruits)

"""splitting by space"""
# sentence="python is awesome"
# words=sentence.split()
# print(words)

"""join()"""
# words=["python","is","awesome"]
# sentence=" ".join(words)
# print(sentence)

"""joining with commas"""
# fruits=["apple","banana","mango"]
# fruits_commas=", ".join(fruits)
# print(fruits_commas)

"""find()"""
# text="hello world"
# find_word=text.find("world")
# print(find_word)

"""count()"""

# text="apple banana apple mango apple"
# print(text.count("apple"))


"""complex data type"""
# c2 = complex(3, -4)  # 3 - 4j
# print(c2)