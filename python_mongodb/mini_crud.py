myDatabase = "database of a collection"


# Insert Arun into the collection.

s ={
    "name": "Arun",
    "age": 22,
    "isActive": True
}

myDatabase.insert_one(s)


# Now retrieve all students whose age is greater than 20.

cursor = myDatabase.find({"age": {"$gt": 20}})

for i in cursor:
    print(i)


# Find the student whose name is "Arun".

find_user = myDatabase.find_one({"name": "Arun"})

print(find_user)


# Now update Arun's age from 22 → 23.

myDatabase.update_one(
    {"name": "Arun"},
    {"$set": {"age": 23}}
)


# Update all students whose age is greater than 50 and set: isActive → False

myDatabase.update_many(
    {"age": {"$gt": 50}},
    {"$set": {"isActive": False}}
)


# Delete only Arun from the collection.

myDatabase.delete_one({"name": "Arun"})