# -*- coding: utf-8 -*-
"""9 - Built-in-functions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PiW8DtqIC7o_dSi1RmJJ7DtE__ZfE92d

#Beginner

###Finding a length
"""

# length
lists = [1, 2, 3, 4, 5, 6, 7]
print(len(lists))

#max value
print(max(lists))

#Convert a number to string
num = 3
print(str(num))

#absalute vallue
value = -262
print(abs(value))

#Round a number
value = 234.6356
print(round(value, 3))

#Sum of list of numbers
list = [1, 2, 3, 4, 5, 9, 8, 7, 4]
print(sum(list))

#Sort in ascending order
list = [5, 21, 45, 21, 7, 1, 21, 3, 554, 23, 11, 122, 1234, 543, 3233, 644, 22, 1]
print(sorted(list))

# Check the data type
null = 12
nul = "string"
nu = 12.22
n = True
print(type(null))
print(type(nul))
print(type(nu))
print(type(n))

# Minimum value of list
print(min(list))

# Convert to Upper
word = "Mohanraj"
print(word.upper())

"""#Intermediate"""

# Flatten a list
lists = [[1, 2, 3, 4], [9, 8, 7], [1, 2, 3, 4, 5], [6, 5, 4, 3]]
print(sum(lists, []))

# List a Even Numbers
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
for i in values:
  if i % 2 == 0:
    even.append(i)
print(even)

# List a Squares of given Numbers
li = [1, 2, 3]
function_1 = list(map(lambda x: x**x, li))
print(function_1)

# sort by second index value
my = [(4, 6), (1,9), (1, 2), (4, 3), (7,4)]
filtered = sorted(my, key = lambda x: x[1])
print(filtered)

# Check given all values of list is positive
# Positive
list1 = [1, 2, 3, 4, 5]
check1 = all(x > 0 for x in list1)
print(check1)

# Negative
list2 = [-1, -2, 3, 5, -4]
check2 = all(x > 0 for x in list2)
print(check2)

# Find if vovels in list
chars = ["a", "b", "c", "d", "e", "f", "g"]
checked1 = any(char in "aeiouAEIOU" for char in chars)
print(checked1)

chars = ["A", "b", "c", "d", "E", "f", "g"]
checked1 = any(char in "aeiouAEIOU" for char in chars)
print(checked1)

chars = ["t", "b", "c", "d", "y", "f", "g"]
checked1 = any(char in "aeiouAEIOU" for char in chars)
print(checked1)

# combine two list into list of tuple
import builtins
lis1 = ["a", "b", "c", "d"]
lis2 = [1, 2, 3, 4]
combined = builtins.list(zip(lis1, lis2))
print(combined)

# print minimum and maximum value in the given list
import builtins
some = [789, 234, 123, 121, 2311, 121, 111, 554, 1211, 21]
print(builtins.min(some))
print(builtins.max(some))

# Total sum of list
digs = [10, 10, 20, 20, 10, 10, 10, 10]
total = sum(digs)
print(total)

# List the index of each elements
import builtins
llist = ["apple", "banana", "Cat", "Dog", "Elephant"]
index_v = builtins.list(enumerate(llist))
print(index_v)

# Reverse a list
import builtins
given = [1, 2, 3, 4, 5, 6, 7, 8, 9]
reversed = builtins.list(reversed(given))
print(reversed)