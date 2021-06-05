# Day 2:

# ASSIGNMENT TO PUSH ON GITHUB

# AGE CALCULATOR
# 1)  calculate Age of a person - User should enter the year of birth and
# the program should output the age.. eg : entered value is 1990, output age is 30

# 2) Simple Calculator:

# 	- get 2 numbers from the user and print the result of addition, subtraction,
#     multiplication and floor division, decimal division, remainder, power of the input numbers

# task 1: Age Calculator
present_year=2021
birth_year=int(input("birth year is : "))
Age=present_year - birth_year

print("age is: ", Age)

# task 2:Simple Calculator

a=int(input("enter number a: "))
b=int(input("enter number b: "))
add=a+b
sub=a-b
multiply=a*b
div1=a/b
div2=a//b
div3=a%b
power_of=a**b

# calculator=(print("sum of a+b: ", add),
# print("sub of a-b: ", sub),
# print("Multiply of a*b: ", multiply),
# print("decimal division of a/b: ", div1),
# print("floor division of a//b: ", div2),
# print("reminder of a%b: ", div3),
# print("power of a**b: ", power_of))


calcultions= (print("a + b = {}".format(a + b)),
print("a - b = {}".format(a - b)),
print("a * b = {}".format(a * b)),
print("a / b = {}".format(a / b)),
print("a % b = {}".format(a % b)),
print("a // b = {}".format(a // b)),
print("a ** b = {}".format(a ** b)) )
