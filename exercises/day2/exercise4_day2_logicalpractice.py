"""
A bank will offer a customer a loan if they are 18 or over and have an annual income of at least $15000. 
Write a program that will, based on a customers age and income, produce a decision on whether they will be offered a loan.
"""

age = int(input("Enter your age: "))
income = int(input("Enter your income: "))

if age >= 18 and income > 15000:
    print("You have been offered a loan")
else:
    print("You do not qualify for a loan")