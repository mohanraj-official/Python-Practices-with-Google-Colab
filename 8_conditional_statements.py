# -*- coding: utf-8 -*-
"""8 - Conditional Statements.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RDm1roxjdtY5AEGNphjFqyGe58AGFd0-

#Beginner

###Simple if statements
"""

x = 5
if x > 4:
  print(f"{x} is Greater than 4")
if x < 6:
  print(f"Now also {x} is lower than 6")

"""###if-elif-statements"""

if x < 5:
  print("X is greater")
else:
  print("X is lesser")

"""###if-else-statements"""

if x < 5:
  print("x is less than 5")
elif x == 5:
  print("x is equal to 5")
else:
  print("x is greater than 5")

"""###Even or odd"""

n = 7
if n % 2 == 0:
  print("This is Even number")
else:
  print("This is Odd number")

"""###Nested if statements"""

n = 10
if n > 0 :
  if n % 2 == 0:
    print("Given value is positive and Even number")

"""###Positive negative or zero"""

g = -4
if g > 0:
  print("Positive")
elif g == 0:
  print("Equal to zero")
else:
  print("Negative")

"""###check if number is divisablle by 3"""

e = 66
if e % 3 == 0 :
  print("Given value is divisible by 3")
else:
  print("Never")

"""###Check the condition"""

d = 12
if d >= 10:
  print("D is larger")

"""###Multiple condition"""

f = 100
if f > 50 and f < 110:
  print("It is True")

"""###Check if list is empty"""

listm = []
if not listm:
  print("List is empty")
else:
  print("List is not Empty")

"""#Intermediate

###Multiple Conditions with and or
"""

z = 25
if z > 20 and z < 30:
  print("It is True")
else:
  print("It is False")

"""###Ternary operator"""

x = 5
result = "postive" if x > 0 else "Negative"
print(result)

"""###Nested if statments"""

n = 35
if n > 50:
  print("Greater than 50")
elif n >= 20:
  print("Value between 20 and 50")
else:
  print("Less than 20")

"""###Multiple factor"""

h = 75
if h % 2 == 0 and h % 3 == 0:
    print("Given number is divisible by 2 and 3")
elif h % 2 == 0:
  print("Given number is divisible by 2")
elif h % 3 == 0:
  print("Given number is divisible by 3")
else:
  print("Give a proper number")

"""###Logical operators and conditions"""

x = 10
if 5 < x < 20 and x % 2 == 0:
  print("Yes is it")
else:
  print("No")

"""###String startswith and endswith"""

txt = "Hello"
if txt.startswith("H") and txt.endswith("o"):
  print("Given String is Correct")
else:
  print("Nope")

"""###Check all elements positive"""

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if all(i > 0 for i in list):
  print("All elements are Positive")
else:
  print("None")

"""###Check palindrome or not"""

user = input("ENter your word : ")
if user == user[::-1]:
  user = user.upper()
  print(f"Given word {user} is a palindrome")
else:
  user = user.upper()
  print(f"given word {user} is not a palindrome")

"""###Nested if"""

age = int(input("Enter your age : "))
if age < 13:
  print("You are a child")
elif 13 <= age < 20:
  print("You are a Teenager")
elif age > 20:
  print("You are Adult")
else:
  print("Invalid input")

"""###Membership operator in condition"""

li = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
choice = int(input("Enter the Value : "))
if choice in li:
  print(f"Given value {choice} is in the list")
else:
  print("Not in list")