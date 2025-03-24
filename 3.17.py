# import numpy as np
#
# # Creating a NumPy array
# arr = np.array([1, 2, 3, 4, 5])
#
# print(arr)
# print(type(arr))  # Output: <class 'numpy.ndarray'>

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6])
# reshaped_arr = arr.reshape(2, 3)  # Convert to 2 rows and 3 columns
#
# print(reshaped_arr)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# transposed_arr = arr.T  # or np.transpose(arr)
#
# print(transposed_arr)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# flattened_arr = arr.flatten()
#
# print(flattened_arr)

# arr = np.array([[1, 2], [3, 4]])
# rotated_arr = np.rot90(arr)  # Rotates counterclockwise
#
# print(rotated_arr)
#
# flipped_v = np.flipud(arr)
# print(flipped_v)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# expanded_arr = np.expand_dims(arr, axis=0)  # Add a new dimension
#
# print(expanded_arr.shape)  # Output: (1, 2, 3)


# print("mahendra")

# print([1, 2, 3, 4])


# print(list(zip((1, 2), (3, 4))))

""""""
"""prime number"""

# def is_prime(n):
#     if n < 2:
#         return False  # Numbers less than 2 are not prime
#     for i in range(2, int(n ** 0.5)+1):  # check divisibility up to sqrt(n)
#         if n % 2 ==0:
#             return False
#         return True
#
# # Example usage
# print(is_prime(7))
# print(is_prime((10)))
#
#
"""2. Print Prime Numbers in a Given Range

"""
# def Prime_numbers_in_range(start,end):
#     primes = []
#     for number in range(start, end+1):
#         if is_prime(number):
#             primes.append(number)
#         return primes
#
# # Example usage
# print(Prime_numbers_in_range(10,50))


""" 3. Generate First N Prime Numbers """

# def first_n_primes(n):
#     primes = []
#     number = 2
#     while len(primes) < n:
#         if is_prime(number):
#             primes.append(number)
#         number +=1
#     return primes
#
# # Example usage
# print(first_n_primes(10))


"""Generate fibonacci sequence upto N Terms"""

# def fibonacci(n):
#     fib_series = [0, 1]
#     for _ in range(n - 2):
#         fib_series.append(fib_series[-1]+fib_series[-2])
#     return fib_series[:n]
# print(fibonacci(10))

"""Armstrong number"""

# def is_armstrong(number):
#     digits = str(number)
#     power = len(digits)
#     total = sum(int(digit) ** power for digit in digits)
#
#     return total == number
#
# # Test the function
# number = int(input("Enter a number: "))
# if is_armstrong(number):
#     print(f"{number} is an armstrong number.")
# else:
#     print(f"{number} is not an armstrong number")

# def is_armstrong(number):
#     digits = str(number)
#     power = len(digits)
#     total = sum(int(digit) ** power for digit in digits)
#
#     return total == number
#
# number = int(input("Enter a number: "))
# if is_armstrong(number):
#     print(f"{number} is an armstrong number.")
# else:
#     print(f"{number} is not a armstrong number")
#

"""list methods"""

# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# print(numbers)

# numbers.extend([7,8,9])
# print(numbers)

# numbers.insert(7,66)
# print(numbers)

# number_index = numbers.index(5)
# print(number_index)

# numbers.remove(5)
# print(numbers)

# numbers.clear()
# print(numbers)

# numbers.pop()
# print(numbers)

# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

# numbers.count(1)
# print(numbers)

# numbers.copy()
# print(numbers)

# numbers.__init__([5])
# print(numbers)

# new_numbers = numbers.__add__([6])
# print(new_numbers)


# numbers = numbers+[6]
# print(numbers)


"""E-commerce system"""

# cart = ["laptop", "mouse", "keyboard"]
#
# cart.append("headphones")
#
# cart.remove("mouse")
#
# if "laptop" in cart:
#     print("laptop is in the cart")
#
# cart.sort()
#
# print(cart)

"""banking system"""

# transactions = [5000, -2000, 3000, -1500, 7000]
#
# last_transaction = transactions[-1]
#
# transactions.append(-500)
#
# balance =sum(transactions)
#
# print("last transaction:",last_transaction)
# print("current balance:",balance)

"""healthcare system"""

# patients = ["john", "Alice", "Bob"]
#
# patients.append("David")
#
# first_patient = patients.pop(0)
#
# print("patient Treated:",first_patient)
# print("Remaining Patients:", patients)

"""IoT smart Home system"""

# devices = ["Light", "Fan", "Tv"]
#
# devices.remove("Fan")
#
# print("Active devices:",devices)
#
# devices.clear()
#
# print(devices)


"Social Media Platform"

# friends = ["Rahul", "Priya", "Vikas"]
#
# friends.append("Aditi")
#
# friends.remove("Priya")
#
# suggested_friend = friends.copy()
#
# print("Friends List:",friends)

"""School management System"""

# students = ["Arun", "Meena", "Ravi"]
#
# students.extend(["Kiran", "Swetha"])
#
# total_students = len(students)
#
# print("Total Students:", total_students)


"""Food Delivery System"""

# orders = ["Pizza", "Burger", "Pasta"]
#
# orders.append("Fries")
#
# orders.pop(0)
#
# print("Remaining Orders:", orders)

"""string methods"""

# customer_name = "John doe"
#
# formatted_name = customer_name.title()
#
# print(formatted_name)

"""MASKING CREDIT CARD NUMBERS"""

# credit_card = "1234567812345678"
#
# masked_card = "*" * 12 + credit_card[-4:]
#
# print(masked_card)

"""Healthcare system"""

# record = "PatientID: 12345, Name: John Doe"
#
# patient_id = record.split(",")[0].split(":")[1].strip()
#
# print(patient_id)

"""IoT Smart Home system"""

# devices_status = "on"
#
# if devices_status.strip().lower() == "on":
#     print("The device is ON.")
# else:
#     print("The device is OFF.")

"""Social Media Platform"""

# comment = "This is a stupid app!"
#
# filtered_comment = comment.replace("stupid","***")
#
# print(filtered_comment)

""" School management System"""

# roll_number = "stu-12345"
#
# if roll_number.upper().startswith("STU"):
#     print("Valid roll number")
# else:
#     print("Invalid roll number")

"""Food Delivery System"""

# customer_name = "Amit"
# order = "Pizza"
# price = 299.99
#
# message = f"Hello {customer_name}, your order for {order} is confirmed. Total:{price:.2f}"
#
# print(message)

"""python pyramids"""

# n = 5
# for i in range(1, n+1):
#     print("*" * i)

# n = 5
# for i in range(1, n+1):
#     print(" "* (n-i) + "*" * i)


"""inverted pyramid"""

# n = 5
# for i in  range(n, 0, -1):
#     print("*" * i)

"""number pyramid"""

# n = 5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

"""Diamond pattern"""

# n = 5
# for i in range(1, n+1, 2):
#     print(" " * ((n-i) // 2) + "*" * i)
# for i in range(n-2, 0,-2):
#     print(" " * ((n-i) // 2) + "*" * i)


# from math import factorial
#
# n = 5
# for i in range(n):
#     for j in range(n - i + 1):
#         print(" ", end="")  # Space formatting
#     for j in range(i + 1):
#         print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
#     print()


""" Finding unique customers """

# customers = {"Amit", "Ravi", "John", "Amit", "Sita", "Ravi"}
#
# unique_customers = set(customers)
#
# print(unique_customers)


"""banking System"""


# loan_customers = {"Rahul", "Amit", "Sita", "Ramesh"}
# credit_card_customers = {"Sita", "Amit", "Pooja", "John"}
#
# common_customers = loan_customers.intersection(credit_card_customers)
#
# print(common_customers)

"""finding patients with common symptoms"""

# fever_patients = {"Ram", "Asha", "Ravi", "John"}
# cough_patients = {"Ravi", "John","Pooja", "Raj"}
#
# patients_with_both = fever_patients & cough_patients
#
# print(patients_with_both)

"""Detecting Unauthorized Access """

# authorized_users = {"Alice", "Bob", "Charlie"}
# login_attempts = {"Charlie", "David", "Bob", "Eve"}
#
# unauthorized_users = login_attempts - authorized_users
#
# print(unauthorized_users)

"""finding students enrolled in only one course"""

# math_students = {"rahul", "Amit", "Ravi"}
# science_students = {"Amit", "Ravi", "Pooja"}
#
# unique_course_students = math_students.symmetric_difference(science_students)
# print(unique_course_students)

"""processing multiple orders"""

# orders = ["order1", "order2", "order3"]
#
# for order in orders:
#     print(f"processing {order}...")

'''monthly interest calculation'''


# balance = 1000
# interest_rate = 0.05
# months = 12
# month = 1
#
# while month <=months:
#     balance +=balance *interest_rate
#     print(f"month {month}: balance = {balance:.2f}")
#     month += 1

"""Grading students Automatically"""
# students = {"Alice":85, "Bob":65, "Charlie":90}
# for student,marks in students.items():
#     if marks >= 90:
#         grade = "A"
#     elif marks >= 75:
#         grade = "B"
#     else:
#         grade = "C"
#     print(f"{student} got grade {grade}")

"""generating bills"""
# items = {"milk": 50, "Bread": 40,"Eggs": 70}
# total = 0
# for item,price in items.items():
#     total += price
#     print(f"{item}: {price}")
# print(f"total Bill: {total}")


"""Checking Available seats"""

# available_seats = ["A1", "A2", "B1", "B2"]
# seat_to_book = "A2"
#
# while seat_to_book in available_seats:
#     available_seats.remove(seat_to_book)
#     print(f"Seat {seat_to_book} book successfully")
#     break

"""Greeting Users Multiple Times"""

# for i in range(3):
#     print("hello! how can I assist you?")


"""lambda functions"""

"""sorting medicines by expiry date"""

# from datetime import datetime
#
# medicines = [
#     {"name": "paracetamol", "expiry": "2025-06-15"},
#     {"name": "Ibuprofen", "expiry": "2024-12-10"},
#     {"name": "Amoxicillin", "expiry": "2023-09-20"}
# ]
#
# sorted_medicines = sorted(medicines,key=lambda x: datetime.strptime(x["expiry"], "%Y-%m-%d"))
# print(sorted_medicines)

# from datetime import datetime
#
# date_str = "2024-03-17 15:30:00"
# date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
#
# print(date_obj)
# print(type(date_obj))  # Output: <class 'datetime.datetime'>
#
# date_str = "17-03-2024"
# date_obj = datetime.strptime(date_str, "%d-%m-%Y")
#
# print("Year:", date_obj.year)
# print("Month:", date_obj.month)
# print("Day:", date_obj.day)


"""Filtering orders by Delivery Status"""
# orders = [
#     {"order_id": 101, "status": "Delivered"},
#     {"order_id": 102, "status": "Pending"},
#     {"order_id": 103, "status": "Delivered"}
# ]
#
# delivered_orders = list(filter(lambda x:x["status"] == "Delivered", orders))
# print(delivered_orders)

# seats = [
#     {"seat_no": "A1", "status": "Booked"},
#     {"seat_no": "A2", "status": "Available"},
#     {"seat_no": "B1", "status": "Available"}
# ]
#
# available_seats = list(filter(lambda x: x["status"] == "Available", seats))
# print(available_seats)




