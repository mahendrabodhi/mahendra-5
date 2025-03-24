"""conditional statements"""


# balance = 5000
# withdraw_amount = int(input("Enter withdrawal amount: "))
#
# if withdraw_amount <= balance:
#     balance -= withdraw_amount
#     print(f"Withdrawal successful! Remaining balance: {balance}")
# else:
#     print("Insufficient balance!")

# stored_username = "admin"
# stored_password = "password123"
#
# username = input("Enter username: ")
# password = input("Enter password: ")
#
# if username == stored_username and password == stored_password:
#     print("Login successful!")
# else:
#     print("Invalid username or password!")

# import time
#
# stored_username = "admin"
# stored_password = "password123"
# attempts = 3
#
# while attempts > 0:
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#
#     if username == stored_username and password == stored_password:
#         print("Login successful!")
#         break
#     else:
#         attempts -= 1
#         if attempts > 0:
#             print(f"Invalid username or password! {attempts} attempts left.")
#         else:
#             print("Too many failed attempts. Try again after 24 hours.")
#             time.sleep(86400)  # Wait for 24 hours (86400 seconds)


# signal = input("Enter traffic signal color (Red/Yellow/Green): ").lower()
#
# if signal == "red":
#     print("Stop!")
# elif signal == "yellow":
#     print("Get Ready!")
# elif signal == "green":
#     print("Go!")
# else:
#     print("Invalid input!")


# temperature = float(input("Enter room temperature (°C): "))
#
# if temperature > 30:
#     print("Warning! High temperature detected.")
# elif temperature < 10:
#     print("Warning! Low temperature detected.")
# else:
#     print("Temperature is normal.")
#
#
# available_seats = 5
# requested_seats = int(input("Enter the number of seats you want to book: "))
#
# if requested_seats <= available_seats:
#     available_seats -= requested_seats
#     print(f"Booking successful! Remaining seats: {available_seats}")
# else:
#     print("Not enough seats available.")
#
# year = int(input("Enter a year: "))
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
#
#
# year = int(input("Enter a year: "))
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
#
# num = int(input("Enter a number: "))
#
# if num > 1:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(f"{num} is not a prime number.")
#             break
#     else:
#         print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")
#
#
# word = input("Enter a word: ")
#
# if word == word[::-1]:
#     print(f"{word} is a palindrome.")
# else:
#     print(f"{word} is not a palindrome.")
#
#
# role = input("Enter your role (admin/user/guest): ").lower()
#
# if role == "admin":
#     print("You have full access.")
# elif role == "user":
#     print("You have limited access.")
# elif role == "guest":
#     print("You have read-only access.")
# else:
#     print("Invalid role!")
#
#
# password = input("Enter a password: ")
#
# if len(password) < 8:
#     print("Weak password! Must be at least 8 characters long.")
# elif not any(char.isdigit() for char in password):
#     print("Weak password! Must contain at least one number.")
# elif not any(char.isupper() for char in password):
#     print("Weak password! Must contain at least one uppercase letter.")
# else:
#     print("Strong password!")

# n = int(input("Enter a number: "))
# total = 0
#
# for i in range(1, n+1):
#     total += i
#
# print(f"Sum of first {n} natural numbers: {total}")

# word = "Python"
# reverse_word=""
# for i in word:
#     reverse_word=i+reverse_word
# print(reverse_word)

# text = "Hello World"
# vowel_count = 0
#
# for char in text.lower():
#     if char in "aeiou":
#         vowel_count += 1
#
# print(f"Total vowels: {vowel_count}")

# num = int(input("Enter a number: "))
# factorial = 1
#
# for i in range(1, num + 1):
#     factorial *= i
#
# print(f"Factorial of {num} is {factorial}")


# num = 1
# while num <= 10:
#     print(num)
#     num += 1


# num = 2
# while num <= 20:
#     print(num, end=" ")
#     num += 2


# maximum = lambda a, b: a if a > b else b
# print(maximum(10, 20))  # Output: 20


