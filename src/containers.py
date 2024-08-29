# Strings
text = "a string"
another_text = 'another string'

print(text + another_text)
print(text + "\n  " + another_text)
print("length of the another_text string is " + str(len(another_text)) + " characters")

# tuples
mytuple = (1, 'hej')
print(mytuple[1])

for i in range(len(mytuple)):
    print(mytuple[i])

# lists
alist = ['a', 2, 'c', 4]

print("length of alist " + str(len(alist)))

# Access the first element
# Index starts at zero
alist[0]

# second element
alist[1]

# Access the last element
alist[-1]

# Access second to last element
alist[-2]

# Select first two elements
alist[0:2]

# Dictionaries - key-value pairs
monthtable = {"Jan": 1, "Feb": 2, "March":3}

# Given a key return the value
monthtable["Jan"]

# Set a new key-value pair
monthtable["April"]=3

# Error
monthtable["Dec"]

