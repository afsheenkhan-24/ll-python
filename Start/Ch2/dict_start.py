# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
mydict = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": [1,2,3,4]
}
print(mydict)

# dictionaries are accessed via keys
print(mydict["two"])
print(mydict["four"])

# you can also set dictionary data by creating a new key
mydict["five"] = 5
print(mydict)


# Trying to access a nonexistent key will produce an error
# print(mydict[6])

# To avoid this, you can use the "in" operator to see if a key exists
print(6 in mydict)
print("two" in mydict)

# You can retrieve all of the keys and values from a dictionary
print(mydict.keys())
print(mydict.values())

# You can also iterate over all the items in a dictionary
for key, val in mydict.items():
  print(key, val)