# l will be representing a list - lists are similar to arrays
l = ["Bob", "Rolf", "Anne"]

# t will be representing a tuple - tuples can't be modifided once instantiated 
t = ("Bob", "Rolf", "Anne")

# s will represent a set -  sets just can't have duplicate eliments.
# lists and tuples keep the same order always with their ellements where as sets dont.
s = {"Bob", "Rolf", "Anne"}

# Printing the first element of the list "Array".
print(l[0])

# Changing the element - note if chaning a tuple an error would be thrown
l[0] = "Smith"
print(l[0])

# Appending a new element to the list, Once again a tuple would thrown an error.
l.append("Larry")
print(l)
l.remove("Smith")
print(l)

#Because sets cant have duplicates there will still only be 1 smith in the set.
s.add("Smith")
s.add("Smith")
print(s)