# -*- coding: utf-8 -*-
"""2 - String Operations and Methods.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17nQgHs4ZEEdkxbn_g630tN4d9H6Qi5G0
"""

s = "hello world"
s.upper()
s.isdigit()
s.find("or")

list = "apple", "orange", "banana"
" - ".join(list)
b = " - ".join(list)
b

s.startswith("hello")

list1 = "apple, banana, orange, mango, grape, blueberry, kiwi, goa, watermelon, strawberry"
list1.split(", ")

a = " apple "
c = a.strip()
b = c.lower()
d = b.upper()
d
d.count('P')
print(d.replace("APPLE", "BANANA"))
word = "national higher secondary svhool"
word.title()

s= "   **vidhjdb221738dsbd**  "
s.isalnum()
s.strip(" *")

ctr = "mohan"
ctr.center(40, "-")

cas = "hello wORLD MOHAMNE sTUDENT hOw dO yIU "
cas.lower().replace("world", "Mohan")

name = "Mohanraj"
age = 16
print(f"Hello I am {name} {age} years world")

lang = "C++, Python, C, Html, CSS, JS, Nodejs, Django"
sorted(lang.split(", "))

free = "HWOlloE worLD "
free.swapcase()
frree = " "
frree.isspace()