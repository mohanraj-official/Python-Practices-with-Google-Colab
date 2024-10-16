# -*- coding: utf-8 -*-
"""6 - Dictionary and it's method.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1js9VfcaRLqdaal6ORHMVILnuNE8hbV1I

#Beginner

###Dictionary Creation
"""

my = {"name" : "Mohan", "age" : 23}
print(my)

"""###Accessing via values"""

new = {"school" : "National Higher Secondary School"}
print(new["school"])

"""###Adding new key-value pairs"""

new["Location"] = "Gudiyattam"
print(new)

"""###Updating a value"""

new["Location"] = "Vellore"
print(new)

"""###Deleting Key-value Paires"""

del(new["Location"])
print(new)

"""###Using get method"""

print(new.get("school"))
print("school" in new)

"""###Getting all keys"""

my = {"name" : "Mohanraj", "age" : 18, "Subject" : "total"}
print(my)
print(my.keys())
print(my.values())

"""###Clear All Details"""

my.clear()
print(my)

"""#Intermediate

###Merging
"""

dic1 = {"name" : "Mohan", "age" : 12}
dic2 = {"nam" : "Raj", "ag" : 21}
dic1.update(dic2)
print(dic1)

"""###Iterate Key and value"""

dic = {"a" : 1, "b" : 2, "c" : 3}
for key, value in dic.items():
  print(f"{key} : {value}")

"""###Dictionary comprihension"""

comp = {key : key**2 for key in range(1, 10)}
print(comp)

"""###pop() and capture"""

captured = comp.pop(9, None)
print(captured)
print(comp)

"""###Set default()"""

doco = {"a" : 1, "b" : 2, "c" : 3}
val = doco.setdefault("d", 4)
print(val)
print(doco)

"""###Creation from two list"""

list1 = ["a", "b", "c"]
list2 = [5, 4, 3]
diction = dict(zip(list1, list2))
print(diction)

"""###Sorting a dictionary"""

uns = {"z" : 3, "x" : 5, "f" : 7, "h" : 1}
sorted = dict(sorted(uns.items()))
print(sorted)

"""###Nested Dictionary"""

nested = {"village" : {"name" : "Mohan"}, "school" : {"name" : "Raj"}}
print(nested)
nested_dict1 = nested["village"]["name"]
print(nested_dict1)
nested_dict2 = nested["school"]["name"]
print(nested_dict2)