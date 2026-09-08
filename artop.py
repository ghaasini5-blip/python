#arithmetic operations
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
 #Setup variables
age = 20
has_id = True
is_suspended = False

# 1. AND Example (Both must be True)
if age >= 18 and has_id:
    print("Eligible to enter the venue.")

# 2. OR Example (At least one must be True)
if age < 12 or age >= 65:
    print("Eligible for a special discount.")

# 3. NOT Example (Inverts a condition)
if not is_suspended:
    print("Account is active and eligible to participate.")

# Combining all three together
# Priority order: 'not' evaluates first, then 'and', then 'or'
if (age >= 18 and has_id) and not is_suspended:
    print("Access fully granted!")#arthimethic operations

#logical operator
age =25
citizen = True

print(age>=18 and citizen == True)
age = 16
citizen = True

print(age>=18 and citizen == True)

has_card = False
has_cash = True

print(has_card or has_cash)

is_logged_in = True

print(not is_logged_in)

#atm eligibility checker
balance = 10000
withdraw = 5000

print(withdraw > 0 and withdraw <= balance)

#student scholarship eligibility checker
marks = float(input("Enter  marks: "))
attendance = float(input("Enter attendance : "))

eligible = marks >= 85 and attendance >= 75
print("scholarship eligibility: ", eligible)

#identity operators
a = None

print(a is None)
print(a is not None)

#bitwise operators
a = 5
b = 3

print(a & b)  
print(a | b)
print(a ^ b)

#electric city bill calculator
units = int(input("Enter electricity units : "))

rate = 6

bill = units * rate

print("Electricity Bill: ", bill)

#travel expence calculator
travel = float(input(" Travel expence: "))
food = float(input("Food expence: "))
hotel = float(input("Hotel expence: "))

total = travel + food + hotel

print("Total Expense: ", total)
