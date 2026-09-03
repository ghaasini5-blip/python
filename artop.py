#arthimethic operations

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("power:", a ** b)

#simple calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#student marks calculator
name = input("Enter student name: ")

m1 = int(input("Enter python marks: "))
m2 = int(input("Enter java marks: "))
m3 = int(input("Enter SQL marks: "))

total = m1 + m2 + m3
average = total / 3

print("\n-----Student Report-----")
print("Name:", name)
print("Total:", total)

#shopping bill calculator
price1 = float(input("Enter price of item 1: "))
price2 = float(input("Enter price of item 2: "))
price3 = float(input("Enter price of item 3: "))

total_price = price1 + price2 + price3

discount = total * 0.10
final_amount = total - discount

print("discount:", discount)
print("final amount:", final_amount)
print("total bill: ", total)

#age eligibility calculator
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")

#assignment operator
x = 10

x += 5 
print(x)

x -= 2
print(x)

x *= 3
print(x)

#bank balance
balance = 10000

deposit = 5000
balance += deposit

print("After Deposit:", balance)

withdraw = 2000
balance -= withdraw

print("After Withdrawal:", balance)
#age eligibility calculator
age = int(input("Enter your age: "))

print ("Eligible:" , age >= 18)

#pass or fail checker
marks = int(input("Enter your marks: "))

print("Passed:", marks >= 40)

