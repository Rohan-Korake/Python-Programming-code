# Create tuple
Left_tuple=(10,20,30,40,50)
Right_tuple=(60,70,80,90,100)

# Accessing
print("Accessing element from left tuple at index 7 : ",Left_tuple[3])

# Concatenation
concat=Left_tuple+Right_tuple
print("Concatenation of left and right tuple : ",(concat))

# Repetition
Repet=Left_tuple*2
print("Repetition of left tuple by 2 : ",Repet)

# Membership
Check=30 in (Left_tuple)
print("Membership of left tuple  : ",Check)

# Length
print("Lenght of left tuple : ",len((Left_tuple)))

# Slicing
print("Slicing of left tuple [1:3] : ",Left_tuple[1:3])
print("Slicing of left tuple [:3]  : ",Left_tuple[:3])
print("Slicing of left tuple [1:]  : ",Left_tuple[1:])
print("Slicing of left tuple [:]   : ",Left_tuple[:])