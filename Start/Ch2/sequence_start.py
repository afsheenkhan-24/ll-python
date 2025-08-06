# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [1, "afsheen", 5, 7, "hamza", True]
print(len(mylist))

# to access a member of a sequence type, use []
print(mylist[1])
print(mylist[-1])
mylist[0] = 30
print(mylist)

# add a list to another list
list1 = [7, 8, 9]
mylist = mylist + list1
print(mylist)

# use slices to get parts of a sequence
print(mylist[1:4:2])
print(mylist[:3:])

# you can use slices to reverse a sequence
print(mylist[::-1])

# Tuples are like lists, but they are immutable (can't be changed)
mytuple = (0, 1, "afsh")
print(mytuple[1])

# Sets are also sequences, but they contain unique values
myset = {1, 2, 3, 4,"afsh", 2}
print(myset)

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print(1 in mylist)
print(5 in mytuple)
print(0 in myset)