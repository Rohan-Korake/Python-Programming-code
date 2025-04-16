# Create two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set 1:", set1)
print("Set 2:", set2)

# Add()
set1.add(7)
print("After add(7):", set1)

# Update()
set1.update([8, 9])
print("After update([8, 9]):", set1)

# Remove()
set1.remove(2)
print("After remove(2):", set1)

# Discard()
set1.discard(10)  # 10 is not in set, no error
print("After discard(10):", set1)

# Pop()
removed_element = set1.pop()
print(f"After pop(): {removed_element} removed, Set1:", set1)

# Clear()
set1.clear()
print("After clear():", set1)

# Subset()
print("Is set1 a subset of set2?", set1.issubset(set2))

# Superset()
print("Is set1 a superset of set2?", set1.issuperset(set2))

