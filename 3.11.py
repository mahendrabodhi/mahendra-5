
"""user input validation"""

# username=input("enter your username: ")
# if username.isalnum():
#     print("Valid username!")
# else:
#     print("Invalid username! only letters and numbers are allowed")

# password = input("enter a password: ")
#
# if (any(char.isupper() for char in password) and
#     any(char.islower() for char in password) and
#     any(char.isdigit() for char in password)):
#     print("strong password!")
# else:
#     print("Weak password! Use a mix of uppercase ,lowercase ,and numbers")

# email = 'mahendra@gmail.com'
# username = email.split('@')[0]
# print('username:', username)



"""count occurrences"""
"""Find how many times "Python" appears in a sentence."""
# sentence = "I Love Python because Python is powerful"
# word_count = sentence.lower().count("python")
# print(word_count)

"""reverse a string"""

# text = input("enter a string: ")
# print("Reversed String:",text[::-1])


"""Format a Receipt with Alignment"""

# item = "Laptop"
# price = 59999
# print(f"{'Item':<10}{'Price':>10}")
# print(f"{item:<10}{price:>10}")


"""Replace Words in a Sentence"""

# review = "This movie is bad.The acting was bad."
# new_review = review.replace("bad","good")
# print(new_review)

"""Extract Digits from string"""

# text = "Order #1234 is placed for $45 on 2024-03-11."
# digits = " ".join(filter(str.isdigit, text))
# print("Extracted Numbers:", digits)

"""Check if a String is a Palindrome"""

# word = input("Enter a word: ")
# if word.lower() == word.lower()[::-1]:
#     print("It is a palindrome!")
# else:
#     print("Not a palindrome")

"""1)Check if a String Contains Only Alphabets"""

# name = input("Enter your name: ")
# if name.isalpha():
#     print("Valid name!")
# else:
#     print("Invalid name! Only alphabets are allowed.")


"2))Convert a Sentence to  Title Case"

# sentence = "python is a popular programming language ."
# title_case = sentence.title()
# print("Title Case:",title_case)


"""Find the First Non-Repeating Character in a string"""

# word = "swiss"
# for char in word:
#     if word.count(char) == 1:
#         print("First non-repeating character:", char)
#         break


"""Generate an Abbreviation for a Phrase"""

# phrase = "Hyper Text Markup Language"
# abbreviation = "".join(word[0] for word in phrase.split()).upper()
# print(abbreviation)

"""Check if Two Words are Anagrams"""

# word1 = "listen"
# word2 = "silent"
#
# if sorted(word1) == sorted(word2):
#     print("They are anagrams!")
# else:
#     print("Not anagrams!")


# card_number = "1234567812345678"
# masked_card = "*" * (len(card_number)-4) + card_number[-4:]
# print(masked_card)

# card="sama"
# card1=card[::-1]
# print(card1)

# word="swiws"
#
# if word == word[::-1]:
#     print("word is palindrome")
# else:
#     print("not palindrome")


# name = "mahendra"
# reversed_name=""
# for char in name:
#     reversed_name=char+reversed_name
# print(reversed_name)


# names=[1,1,2,2,3,3]
# original_list=[]
# for i in names:
#     if i not in  original_list:
#         original_list.append(i)
# print(original_list)





# name=input("enter username: ")
# password_=input("enter password: ")
#
# username="mahendra"
# password="123"
#
# if username == name and password==password_:
#     print("login successful")
# else:
#     print("invalid credentials")


# product1, qty1, price1 = "Keyboard", 5, 1200
# product2, qty2, price2 = "Mouse", 10, 600
#
# print(f"{'Product':<12}{'Qty':>5}{'Price':>10}")
# print(f"{product1:<12}{qty1:>5}{price1:>10}")
# print(f"{product2:<12}{qty2:>5}{price2:>10}")

# train1, time1 = "Express 101", "10:30 AM"
# train2, time2 = "Superfast 202", "12:15 PM"
#
# print(f"{'Train Name':<20}{'Departure':>15}")
# print(f"{train1:<20}{time1:>15}")
# print(f"{train2:<20}{time2:>15}")


print(f"{"time":>15}")
           