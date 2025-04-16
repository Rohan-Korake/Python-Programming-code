# Create Dictionary
my_dict={"Name":"Jerry","Age":18,"City":"Sangli"}
print("Dictionary content : ",my_dict)

# Accessing value
print("Name : ",my_dict["Name"])

# Adding value
my_dict["Email"]="jerry@gmail.com"
print(print("Dictionary content : ",my_dict))

# Updating value
my_dict["Age"]=17
print(print("Dictionary content : ",my_dict))

# Deleting value
del my_dict["Email"]
print(print("Dictionary content : ",my_dict))

# Checking value
if "Name" in my_dict:
    print("Name key present in dictionary")

# Looping
for key in my_dict:
    print(key,":",my_dict[key])

# Length
print("Length of dictionary : ",len(my_dict))

# Clear
print("After clear all dictionary content : ",my_dict.clear())