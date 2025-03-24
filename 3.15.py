"""validation phone number"""
"""validation phone number"""
import re
#
# def validate_phone_number(number):
#     pattern = r"^[6-9]\d{9}$"  # Starts with 6,7,8,9 and has 10 digits
#     return bool(re.fullmatch(pattern, number))
#
# # Test cases
# print(validate_phone_number("9876543210"))  # ✅ True (Valid)
# print(validate_phone_number("1234567890"))  # ❌ False (Invalid)
# print(validate_phone_number("98765"))       # ❌ False (Invalid)


# pattern = r"^[6-9]\d{9}$"
#
# # test cases
#
# numbers = ["9966998877","6123457896","5123654785","7845123698","4578963214"]
#
# for number in numbers:
#     if re.match(pattern,number):
#         print(f"{number} is a valid mobile number")
#     else:
#         print(f"{number} is not a valid mobile number")



# import os
# print(os.listdir())  # Lists files in the current directory


# import math
#
# number = math.sqrt(121)
# print(number)

# import random
# print(random.randint(1, 100))  # Random number between 1 and 100

# from captcha.image import ImageCaptcha
#
# image = ImageCaptcha(width=280, height=90)
# captcha_text = "X9A7B"  # Random text for CAPTCHA
# image.generate(captcha_text)
# image.write(captcha_text, "captcha.png")  # Saves as an image
#
# print("CAPTCHA saved as captcha.png")

# from PIL import Image, ImageDraw, ImageFont
# import random
#
# # Create an image with white background
# width, height = 200, 80
# image = Image.new("RGB", (width, height), "white")
# draw = ImageDraw.Draw(image)
#
# # Generate random text
# captcha_text = "".join(random.choices("ABCDEFGHJKLMNPQRSTUVWXYZ23456789", k=6))
#
# # Add text to image
# font = ImageFont.load_default()
# draw.text((50, 30), captcha_text, fill="black", font=font)
#
# # Save the image
# image.save("custom_captcha.png")
# print(f"Custom CAPTCHA Generated: {captcha_text}")


"""
-----------------------General purpose--------------------------

import sys  # System-specific parameters and functions
import os   # Interacting with the operating system
import time  # Time-related functions
import datetime  # Date and time manipulation
import random  # Generate random numbers
import math  # Mathematical functions
import functools  # Higher-order functions and decorators
import itertools  # Iterators for efficient looping
"""

"""
---------------File handling & os interaction------------------------

import shutil  # File and directory management
import pathlib  # Object-oriented filesystem paths
import tempfile  # Temporary file handling

"""

"""
--------------------------Data Handling & Processing--------------------

import json  # Working with JSON data
import csv  # Read and write CSV files
import xml.etree.ElementTree as ET  # XML processing
import re  # Regular expressions for pattern matching
import collections  # Specialized container datatypes
import hashlib  # Hash functions (MD5, SHA, etc.)

"""

"""
-------------------Networking & Web Scraping---------------------------


import requests  # HTTP requests (external library)
import urllib  # URL handling
import socket  # Networking and communication
import http.server  # Create an HTTP server
import smtplib  # Sending emails
import ftplib  # File Transfer Protocol (FTP)
import html.parser  # Parsing HTML
import xmlrpc.client  # XML-RPC protocol for remote procedure calls

"""

"""
--------------------Threading &Multiprocessing-------------------------- 

import threading  # Multithreading
import multiprocessing  # Parallel processing
import asyncio  # Asynchronous programming

"""

"""
-----------------GUI Development-----------------------------

import tkinter  # Basic GUI applications
import PyQt5  # Advanced GUI (external)
import PySide6  # Alternative to PyQt (external)

"""

"""

-------------Scientific Computing & Data Analysis------------------------

import numpy as np  # Numerical computations (external)
import pandas as pd  # Data analysis (external)
import scipy  # Scientific computing (external)

"""

"""
----------------Machine Learning & AI-----------------

import tensorflow as tf  # Deep learning (external)
import keras  # Neural networks (external)
import sklearn  # Machine learning (external)
import torch  # PyTorch deep learning framework (external)

"""
"""_________________________________"""

"""------------Game development& Graphics-------------

import pygame  # Game development (external)
import turtle  # Simple graphics and animations


"""

"""
-------------Security & Cryptography----

import cryptography  # Cryptographic functions (external)
import secrets  # Secure random numbers for passwords and tokens
import hmac  # Hash-based message authentication codes

"""

"""
 ------------Checking Installed Modules------------

help("modules")

"""

# help("modules")

import  re

# email = "mahendra@gamil.com"
# print(email)

"""email validation"""

# import re
#
# email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$"
#
# emails = ["test.email@example.com", "user123@domain.co", "wrong.email@com", "@missingusername.com"]
#
# for email in emails:
#     if re.match(email_pattern,email):
#         print(f"valid:{email}")
#     else:
#         print(f"invalid:{email}")
#


# def is_valid_email(email):
#     # Check if '@' is present exactly once
#     if email.count('@') != 1:
#         return False
#
#     # Split into username and domain parts
#     username, domain = email.split('@')
#
#     # Check if both username and domain are not empty
#     if not username or not domain:
#         return False
#
#     # Check if '.' is present in the domain
#     if '.' not in domain:
#         return False
#
#     # Check if the domain extension is at least 2 characters long
#     domain_parts = domain.split('.')
#     if len(domain_parts[-1]) < 2:
#         return False
#
#     # Check for invalid characters
#     valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-"
#     for char in username:
#         if char not in valid_chars:
#             return False
#
#     return True
#
# # Testing the function
# emails = ["test.email@example.com", "user123@domain.co", "wrong.email@com", "@missingusername.com", "user@domain..com"]
#
# for email in emails:
#     if is_valid_email(email):
#         print(f"✅ Valid: {email}")
#     else:
#         print(f"❌ Invalid: {email}")
