#  7. List Manipulation: Add and Remove

# Practice Problem: Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

fruits.append("fig")
fruits.pop(1)

print(fruits)