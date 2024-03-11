#Tuples-cannot be changed/modified
coordinates = (4, 5)
print(coordinates[0])

#Functions

def say_hi(name, age):
    print("Hello " + name + ", you are " + age)

say_hi("Paul", "23")
say_hi("John", "36")

#Return Statement

def cube(num):
    return num*num*num
result = cube(3)
print(cube(3))

#If statements

is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither a male nor tall")

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not male but are tall")
else:
    print("You are not a male or tall")

#If statements and comparisons

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300, 40, 5))


#Building a better calculator

num1 = float(input("Enter first number: "))
op = input("Enter first operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")


#Dictionaries

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])
print(monthConversions.get("Dec"))

#While loop

i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")


