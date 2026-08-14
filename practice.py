# ============================================================
# Part A: for Loop Practice (15 Questions)
# ============================================================

# Beginner

# 1. Print numbers from 1 to 100.

n = 100

for i in range(1, n + 1):
    print(i, end=", ")

print()


# ============================================================
# 2. Print numbers from 100 to 1.
# ============================================================

n = 100

for i in range(n, 0, -1):
    if i == 1:
        print(i)
    else:
        print(i, end=", ")


# ============================================================
# 3. Print all even numbers from 1 to 100.
# ============================================================

n = 100

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")

print()


# ============================================================
# 4. Print all odd numbers from 1 to 100.
# ============================================================

n = 100

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")

print()


# ============================================================
# 5. Find the sum of first N numbers.
# ============================================================

n = int(input("Enter the value of n: "))

val = 0

for i in range(1, n + 1):
    val += i

print("Sum =", val)


# ============================================================
# 6. Find the factorial of a number.
# ============================================================

n = int(input("Enter the value of n: "))

val = 1

for i in range(1, n + 1):
    val *= i

print("Factorial =", val)


# ============================================================
# 7. Print the multiplication table of a given number.
# ============================================================

n = int(input("Enter the value of n: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")


# ============================================================
# 8. Find the sum of digits of a number.
# ============================================================

digit = int(input("Enter a number: "))

val = 0

for i in str(digit):
    val += int(i)

print("Sum of digits =", val)


# ============================================================
# 9. Count the number of digits in a number.
# ============================================================

digit = int(input("Enter a number: "))

count = 0

for i in str(digit):
    count += 1

print("Number of digits =", count)


# ============================================================
# 10. Reverse a number.
# ============================================================

n = int(input("Enter a number: "))

rev = 0

for i in str(n):
    rev = int(i) + rev * 10

print("Reversed number =", rev)


# ============================================================
# Intermediate
# ============================================================


# ============================================================
# 11. Check whether a number is Prime.
# ============================================================

n = int(input("Enter a number: "))

if n < 2:
    print("Not prime")
else:
    is_prime = True

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Is prime")
    else:
        print("Not prime")


# ============================================================
# 12. Print all Prime numbers between 1 and N.
# ============================================================

n = int(input("Enter a number: "))

for num in range(2, n + 1):

    is_prime = True

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

print()


# ============================================================
# 13. Find the GCD (HCF) of two numbers.
# ============================================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD (HCF) =", gcd)


# ============================================================
# 14. Find the LCM of two numbers.
# ============================================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(max(a, b), a * b + 1):
    if i % a == 0 and i % b == 0:
        lcm = i
        break

print("LCM =", lcm)


# ============================================================
# 15. Generate the Fibonacci series.
# ============================================================

n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()

# ============================================================
# Python Loop Practice
# Part B: while Loop + Additional Practice
# ============================================================


# ============================================================
# BEGINNER - WHILE LOOP
# ============================================================

# 1. Print numbers from 1 to N

n = 100
i = 1

while i <= n:
    print(i, end=" ")
    i += 1

print()


# 2. Print numbers from N to 1

n = 100

while n >= 1:
    print(n, end=" ")
    n -= 1

print()


# 3. Print even numbers using while loop

n = 100
i = 1

while i <= n:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1

print()


# 4. Print odd numbers using while loop

n = 100
i = 1

while i <= n:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1

print()


# 5. Find the sum of first N numbers

n = int(input("Enter N: "))

total = 0

while n > 0:
    total += n
    n -= 1

print("Sum =", total)


# 6. Find factorial using while loop

n = int(input("Enter a number: "))

factorial = 1

while n > 0:
    factorial *= n
    n -= 1

print("Factorial =", factorial)


# 7. Reverse a number

n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print("Reverse =", reverse)


# 8. Count the number of digits

n = int(input("Enter a number: "))

count = 0

while n > 0:
    count += 1
    n //= 10

print("Number of digits =", count)


# 9. Find the sum of digits

n = int(input("Enter a number: "))

total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10

print("Sum of digits =", total)


# 10. Check whether a number is a palindrome

n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# ============================================================
# INTERMEDIATE - WHILE LOOP
# ============================================================

# 11. Guess the number game

secret_number = 7

guess = int(input("Guess the number: "))

while guess != secret_number:
    print("Wrong guess!")
    guess = int(input("Guess again: "))

print("You guessed the correct number!")


# 12. Password validation

correct_password = "python123"

password = input("Enter your password: ")

while password != correct_password:
    print("Incorrect password!")
    password = input("Enter your password: ")

print("Password correct!")


# 13. ATM menu

balance = 10000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("Amount deposited successfully.")
        print("New balance =", balance)

    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal successful.")
            print("Remaining balance =", balance)
        else:
            print("Insufficient balance.")

    elif choice == 4:
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice.")


# 14. Read numbers until the user enters 0

num = int(input("Enter a number: "))

while num != 0:
    print("You entered:", num)
    num = int(input("Enter another number (0 to stop): "))

print("Program ended.")


# 15. Search an element in a list using while loop

nums = [10, 20, 30, 40, 50]

search = int(input("Enter the element to search: "))

i = 0
found = False

while i < len(nums):
    if nums[i] == search:
        found = True
        break

    i += 1

if found:
    print("Element found at index:", i)
else:
    print("Element not found.")


# ============================================================
# ADDITIONAL LOOP PRACTICE
# ============================================================

# 16. Find GCD of two numbers

a = int(input("Enter a: "))
b = int(input("Enter b: "))

gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD =", gcd)


# 17. Print all prime numbers from 1 to N

n = int(input("Enter N: "))

for num in range(2, n + 1):

    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

print()


# 18. Check whether a number is prime

n = int(input("Enter a number: "))

is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")


# 19. Check whether a string is a palindrome

text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# 20. Print odd numbers from 1 to 100

for i in range(1, 101, 2):
    print(i, end=" ")

print()


# 21. Add an element to a list

my_list = [10, 20, 30, 40, 50]

my_list.append(60)

print(my_list)

# ============================================================
# PYTHON OOP PRACTICE
# ============================================================

# 1.
# Create a Student class with:
# - name
# - age
# - display() method to print details.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


name = input("Enter your name: ")
age = int(input("Enter your age: "))

student1 = Student(name, age)
student1.display_info()


# ============================================================


# 2.
# Create a Car class with:
# - brand
# - model
# - start() method.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"Car: Brand = {self.brand}, Model = {self.model}")


brand = input("Enter the car brand: ")
model = input("Enter the car model: ")

car1 = Car(brand, model)
car1.start()


# ============================================================


# 3.
# Create an Employee class using a constructor to initialize:
# - employee_id
# - employee_name
# - salary
# Print all details.

class Employee:
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary


emp_id = int(input("Enter employee ID: "))
emp_name = input("Enter employee name: ")
salary = int(input("Enter salary: "))

emp1 = Employee(emp_id, emp_name, salary)

print(f"Employee ID: {emp1.emp_id}")
print(f"Employee Name: {emp1.emp_name}")
print(f"Salary: {emp1.salary}")


# ============================================================


# 4.
# Create a Mobile class with:
# - brand
# - price
# Write a method to display the details.

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print(f"Mobile Brand: {self.brand}")
        print(f"Price: {self.price}")


brand = input("Enter brand: ")
price = int(input("Enter price: "))

mobile1 = Mobile(brand, price)
mobile1.display()


# ============================================================


# 5.
# Create a Book class with:
# - title
# - author
# - price
# Display all information.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


title = input("Enter book title: ")
author = input("Enter book author: ")
price = int(input("Enter book price: "))

book1 = Book(title, author, price)

print(f"Title: {book1.title}")
print(f"Author: {book1.author}")
print(f"Price: {book1.price}")


# ============================================================


# 6.
# Create two Student objects and print their names and marks.

class StudentMarks:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


name1 = input("Enter name of student 1: ")
marks1 = int(input("Enter marks of student 1: "))

student1 = StudentMarks(name1, marks1)

name2 = input("Enter name of student 2: ")
marks2 = int(input("Enter marks of student 2: "))

student2 = StudentMarks(name2, marks2)

student1.display()
student2.display()


# ============================================================


# 7.
# Create a Laptop class with:
# - brand
# - RAM
# - processor
# Display all values.

class Laptop:
    def __init__(self, brand, ram, processor):
        self.brand = brand
        self.ram = ram
        self.processor = processor

    def display(self):
        print(f"Laptop Brand: {self.brand}")
        print(f"RAM: {self.ram}")
        print(f"Processor: {self.processor}")


brand = input("Enter brand: ")
ram = input("Enter RAM: ")
processor = input("Enter processor: ")

laptop1 = Laptop(brand, ram, processor)
laptop1.display()


# ============================================================


# 8.
# Create a Movie class with:
# - movie name
# - hero
# - rating
# Print movie details.

class Movie:
    def __init__(self, movie_name, hero, rating):
        self.name = movie_name
        self.hero = hero
        self.rating = rating

    def display(self):
        print(f"Movie: {self.name}")
        print(f"Hero: {self.hero}")
        print(f"Rating: {self.rating}")


name = input("Enter movie name: ")
hero = input("Enter hero name: ")
rating = float(input("Enter rating: "))

movie1 = Movie(name, hero, rating)
movie1.display()


# ============================================================


# 9.
# Create a Bank class with:
# - account number
# - account holder name
# Display the details.

class Bank:
    def __init__(self, acc_number, acc_holder_name):
        self.acc_number = acc_number
        self.acc_holder_name = acc_holder_name

    def display(self):
        print(f"Account Number: {self.acc_number}")
        print(f"Account Holder Name: {self.acc_holder_name}")


acc_number = input("Enter account number: ")
acc_holder_name = input("Enter account holder name: ")

bank1 = Bank(acc_number, acc_holder_name)
bank1.display()


# ============================================================


# 10.
# Create a Hospital class with:
# - patient name
# - disease
# Display patient details.

class Hospital:
    def __init__(self, patient_name, disease):
        self.patient_name = patient_name
        self.disease = disease

    def display(self):
        print(f"Patient Name: {self.patient_name}")
        print(f"Disease: {self.disease}")


patient_name = input("Enter patient name: ")
disease = input("Enter disease: ")

hospital1 = Hospital(patient_name, disease)
hospital1.display()


# ============================================================


# 11.
# Create a BankAccount class with a private variable __balance
# and print it using a getter method.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def display_balance(self):
        print(f"Balance: {self.get_balance()}")


balance = float(input("Enter initial balance: "))

account = BankAccount(balance)

account.display_balance()


# ============================================================


# 12.
# Create a setter method to update the private balance.

class BankAccountSetter:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def display_balance(self):
        print(f"Balance: {self.get_balance()}")


balance = float(input("Enter initial balance: "))
new_balance = float(input("Enter new balance: "))

account = BankAccountSetter(balance)

account.set_balance(new_balance)
account.display_balance()


