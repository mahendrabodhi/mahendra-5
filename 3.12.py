""""""

"""MVT -model-view-template"""

"""MVT-PATTERN"""

# for number in range(10):
#     if number % 2 == 0:
#         print("even number  :", number)
#     else:
#         print("number is odd:", number)


# numbers = [1, 2, 3, 4, 5, 6]
# print(numbers)

# numbers.append(10)
# print(numbers)
#
# numbers.extend([11,12,13])
# print(numbers)
#
# numbers.insert(1,0)
# print(numbers)

"""create variable for index"""
# indexing = numbers.index(5)
# print(indexing)
#
# numbers.reverse()
# print(numbers)
#
# numbers.remove(5)
# print(numbers)

"""create variable for count"""
# number_count = numbers.count(11)
# print(number_count)


# numbers.clear()
# print(numbers)

# numbers.sort()
# print(numbers)


"""enumerate"""
# fruits = ["Apple", "Banana", "Cherry"]

# for index, fruit in enumerate(fruits,start=1):
#     print(f"{index}. {fruit}")


# import tkinter as tk
#
# def on_click(button_text):
#     if button_text == "=":
#         try:
#             result = str(eval(entry_var.get()))
#             entry_var.set(result)
#         except Exception:
#             entry_var.set("Error")
#     elif button_text == "C":
#         entry_var.set("")
#     else:
#         entry_var.set(entry_var.get() + button_text)
#
# # Create main window
# root = tk.Tk()
# root.title("Calculator")
# root.geometry("300x400")
#
# entry_var = tk.StringVar()
# entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify='right')
# entry.pack(fill='both', padx=10, pady=10)
#
# buttons = [
#     ("7", "8", "9", "/"),
#     ("4", "5", "6", "*"),
#     ("1", "2", "3", "-"),
#     ("C", "0", "=", "+")
# ]
#
# for row in buttons:
#     frame = tk.Frame(root)
#     frame.pack(expand=True, fill='both')
#     for char in row:
#         button = tk.Button(frame, text=char, font=("Arial", 20), command=lambda c=char: on_click(c))
#         button.pack(side='left', expand=True, fill='both')
#
# root.mainloop()


# import tkinter as tk
# from tkinter import messagebox
#
# students = []
#
#
# # Function to add student details
# def add_student():
#     if len(students) >= 100:
#         messagebox.showwarning("Limit Reached", "Cannot add more than 100 students.")
#         return
#
#     name = name_var.get()
#     age = age_var.get()
#     roll_no = roll_var.get()
#     class_name = class_var.get()
#     marks = marks_var.get()
#
#     if name and age and roll_no and class_name and marks:
#         students.append({"Name": name, "Age": age, "Roll No": roll_no, "Class": class_name, "Marks": marks})
#         messagebox.showinfo("Success", "Student added successfully!")
#         name_var.set("");
#         age_var.set("");
#         roll_var.set("");
#         class_var.set("");
#         marks_var.set("")
#     else:
#         messagebox.showwarning("Input Error", "Please fill all fields.")
#
#
# # Function to display students
# def show_students():
#     student_list.delete(0, tk.END)
#     for i, student in enumerate(students):
#         student_list.insert(tk.END, f"{i + 1}. {student['Name']} - {student['Roll No']}")
#
#
# def view_details():
#     try:
#         selected = student_list.curselection()[0]
#         student = students[selected]
#         messagebox.showinfo("Student Details",
#                             f"Name: {student['Name']}\nAge: {student['Age']}\nRoll No: {student['Roll No']}\nClass: {student['Class']}\nMarks: {student['Marks']}")
#     except IndexError:
#         messagebox.showwarning("Selection Error", "Please select a student from the list.")
#
#
# # Creating main window
# root = tk.Tk()
# root.title("Student Management App")
# root.geometry("400x500")
#
# # Variables
# name_var = tk.StringVar()
# age_var = tk.StringVar()
# roll_var = tk.StringVar()
# class_var = tk.StringVar()
# marks_var = tk.StringVar()
#
# # Entry Fields
# tk.Label(root, text="Name:").pack()
# tk.Entry(root, textvariable=name_var).pack()
# tk.Label(root, text="Age:").pack()
# tk.Entry(root, textvariable=age_var).pack()
# tk.Label(root, text="Roll No:").pack()
# tk.Entry(root, textvariable=roll_var).pack()
# tk.Label(root, text="Class:").pack()
# tk.Entry(root, textvariable=class_var).pack()
# tk.Label(root, text="Marks:").pack()
# tk.Entry(root, textvariable=marks_var).pack()
#
# # Buttons
# tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
# tk.Button(root, text="Show Students", command=show_students).pack(pady=5)
# tk.Button(root, text="View Details", command=view_details).pack(pady=5)
#
# # Student Listbox
# student_list = tk.Listbox(root)
# student_list.pack(fill=tk.BOTH, expand=True)
#
# root.mainloop()


# import tkinter as tk
# from tkinter import messagebox
#
# # Sample product data (100 items from various categories)
# products = [
#     {"Name": "Apple", "Price": "2$/kg", "Quantity": "50", "Quality": "Fresh", "Category": "Groceries"},
#     {"Name": "Banana", "Price": "1$/dozen", "Quantity": "100", "Quality": "Fresh", "Category": "Groceries"},
#     {"Name": "Rice", "Price": "20$/bag", "Quantity": "30", "Quality": "Premium", "Category": "Groceries"},
#     {"Name": "Laptop", "Price": "700$", "Quantity": "10", "Quality": "Brand New", "Category": "Electronics"},
#     {"Name": "Smartphone", "Price": "500$", "Quantity": "20", "Quality": "Latest Model", "Category": "Electronics"},
#     {"Name": "Table", "Price": "100$", "Quantity": "15", "Quality": "Wooden", "Category": "Furniture"},
#     {"Name": "Chair", "Price": "50$", "Quantity": "40", "Quality": "Plastic", "Category": "Furniture"},
#     {"Name": "Sofa", "Price": "300$", "Quantity": "5", "Quality": "Luxury", "Category": "Furniture"},
#     {"Name": "Cooking Oil", "Price": "10$/litre", "Quantity": "50", "Quality": "Refined", "Category": "Kitchen Items"},
#     {"Name": "Blender", "Price": "60$", "Quantity": "10", "Quality": "Electric", "Category": "Kitchen Items"},
#     {"Name": "Microwave", "Price": "150$", "Quantity": "8", "Quality": "Brand New", "Category": "Kitchen Items"},
#     {"Name": "Frying Pan", "Price": "25$", "Quantity": "30", "Quality": "Non-stick", "Category": "Utensils"},
#     {"Name": "Dinner Set", "Price": "40$", "Quantity": "20", "Quality": "Ceramic", "Category": "Utensils"},
#     {"Name": "Notebook", "Price": "3$/piece", "Quantity": "200", "Quality": "Premium", "Category": "Books"},
#     {"Name": "Blender", "Price": "60$", "Quantity": "10", "Quality": "Electric", "Category": "Kitchen Items"},
#     {"Name": "vanta", "Price": "150$", "Quantity": "8", "Quality": "Brand New", "Category": "Kitchen Items"},
#     {"Name": "hello", "Price": "25$", "Quantity": "30", "Quality": "Non-stick", "Category": "Utensils"},
#     {"Name": "Dinner Set", "Price": "40$", "Quantity": "20", "Quality": "Ceramic", "Category": "Utensils"},
#     {"Name": "Notebook", "Price": "3$/piece", "Quantity": "200", "Quality": "Premium", "Category": "Books"},
#     {"Name": "Story Book", "Price": "10$/book", "Quantity": "100", "Quality": "Bestseller", "Category": "Books"},
#
#     {"Name": "Story Book", "Price": "10$/book", "Quantity": "100", "Quality": "Bestseller", "Category": "Books"},
# ]
#
#
# # Function to search for a product
# def search_product():
#     query = search_var.get().lower()
#     result_list.delete(0, tk.END)
#     found = False
#
#     for product in products:
#         if query in product["Name"].lower():
#             result_list.insert(tk.END, f"{product['Name']} ({product['Category']})")
#             found = True
#
#     if not found:
#         messagebox.showinfo("Not Found", "No matching products found.")
#
#
# # Function to show product details
# def show_details():
#     try:
#         selected = result_list.curselection()[0]
#         product_name = result_list.get(selected).split(" (")[0]
#
#         for product in products:
#             if product["Name"] == product_name:
#                 messagebox.showinfo(
#                     "Product Details",
#                     f"Name: {product['Name']}\nCategory: {product['Category']}\nPrice: {product['Price']}\nQuantity: {product['Quantity']}\nQuality: {product['Quality']}"
#                 )
#                 break
#     except IndexError:
#         messagebox.showwarning("Selection Error", "Please select a product from the list.")
#
#
# # Creating main window
# root = tk.Tk()
# root.title("E-commerce Product Search")
# root.geometry("500x600")
# root.configure(bg="#f4f4f4")
#
# # Title Label
# tk.Label(root, text="E-commerce Store", font=("Arial", 18, "bold"), bg="#f4f4f4").pack(pady=10)
#
# # Search bar
# tk.Label(root, text="Search Product:", font=("Arial", 12), bg="#f4f4f4").pack()
# search_var = tk.StringVar()
# tk.Entry(root, textvariable=search_var, font=("Arial", 12)).pack()
# tk.Button(root, text="Search", font=("Arial", 12, "bold"), command=search_product, bg="#007BFF", fg="white").pack(
#     pady=5)
#
# # Results listbox
# result_list = tk.Listbox(root, font=("Arial", 12), height=10)
# result_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
#
# # Show details button
# tk.Button(root, text="View Details", font=("Arial", 12, "bold"), command=show_details, bg="#28A745", fg="white").pack(
#     pady=5)
#
# root.mainloop()


