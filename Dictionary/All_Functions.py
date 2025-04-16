my_dict={"Name":"Jerry","Age":18,"City":"Sangli"}
print("Dictionary content : ",my_dict)

# Copy()
copied=my_dict.copy()
print("Copied dictionary : ",copied)

# Get(key)
print("Name : ",my_dict.get("Name"))

# Items()
print("Items:", my_dict.items())

# Keys()
print("Keys : ",my_dict.keys())

# Values()
print("Values : ",my_dict.values())

# Pop()
my_dict.pop("Age")
print("After pop dictionary :",my_dict)

# Popitem()
my_dict.popitem()
print("After popitem dictionary :",my_dict)

# setdefault
my_dict.setdefault("email", "jerry@mail.com")
print("After setdefault:", my_dict)

# fromkeys()
new_dict = dict.fromkeys(["a", "b", "c"], 0)
print("From keys:", new_dict)

