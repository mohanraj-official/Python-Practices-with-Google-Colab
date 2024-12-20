# -*- coding: utf-8 -*-
"""13 - Excption Handling.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jm3gsmMpXc3pKzrqZQOstlLoxuWoZ_vX

#Beginner
"""

# o Devision error
try:
  numerator = int(input("Enter the Numerator value : "))
  denominator = int(input("Enter the Denominator value : "))
  result = numerator / denominator
  print(f"The result is  {result}")
except ZeroDivisionError:
  print("Sorry Cannot Divide the numerator by 0")
except ValueError:
  print("Give the Proper Input")

try:
  inp = int(input("Enter the Value : "))
  print(f"You are enetered {inp}.")

except ValueError:
  print("Error : Pleas Enter a valid input")

#Index Error and ValueError
print("Please Enter the 5 numbers")
input_list = []
try:
  for i in range(1, 6):
    inp = int(input(f"Enter Number {i} : "))
    input_list.append(inp)
  integer = int(input("Please Enter any integer between 0-4 : "))
  print(f"you were entered list : {input_list}, then integer and value is {integer} : {input_list[integer]}")
except IndexError:
  print("Error : Please Enter a valid index")

except ValueError:
  print("Error : Please enter the valid numbers!")

#FileNotFoundError
from google.colab import files
uploaded = files.upload()
try:
  userfile = input("Enter the File name : ")
  with open(userfile, "r") as file:
    content = file.read()
    print(content)
except FileNotFoundError:
  print("Error : Please Put a Proper FileName..")

#Creating Own Error Class -- NegativeNumberError
class NegativeNumberError(Exception):
  pass

try:
  user = int(input("Enter the Positive Number : "))
  if user < 0:
    raise NegativeNumberError("Error : Please Enter a valid Input like positive Number")
  else:
    print(f"You were entered : {user}")

except NegativeNumberError as e:
  print(e)

#KeyError
phonebook = {
    "Mohanraj" : "82489 59404",
    "Vignesh" : "88258 68589",
    "Subramani" : "78458 28485",
    "Sajith" : "90802 80401",
    "Mahalakshmi" : "63690 60416"
}

try:
  name = input("Enter the name of you are finding : ")
  print(f"Phone Number of {name} is '{phonebook[name]}'")
except KeyError:
  print("Sorry there is no person in this name - Please try again:")

#ValueError In list
try:
  input_list = input("Enter the Strings you want to put : ").split()
  print(input_list)
  user_to_remove = input("Enter which you want to remove : ")
  input_list.remove(user_to_remove)
  print(f"User wants to removal item is '{user_to_remove}' and \nThe balance list is {input_list}")

except ValueError:
  print("Error : Please enter a proper Strings to remove")

# Attribute Error
class car:
  def start_engine(self):
    print("Engine Started")
try:
  mohanraj = car()
  mohanraj.start_engine()
  mohanraj.start_eng()

except AttributeError:
  print("Error : No attribute found named start_eng()")

#Value Error and ZeroDivisionError
input1 = int(input("Enter the number 1 : "))
input2 = int(input("Enter the number 2 : "))

try:
  answer = input1 / input2
  print(f"{input1} / {input2} = {answer}")
except (ValueError, ZeroDivisionError):
  print("Error: Invalid Input or Division By zero")