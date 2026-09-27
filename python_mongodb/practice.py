mycollection = "collection of database"

# Find documents where age is greater than 30

result = mycollection.find({"age":{"$gt":30}})

# Find all users whose age is greater than 20 AND less than 60.

result = mycollection.find({"age":{"$gt":20, "$lt":60}})

# Find users whose age is either 10, 17, or 25.

result = mycollection.find({"age":{"$in":[10, 17, 25]}})

# Find users where isActive is True OR age is less than 18.

result = mycollection.find({"$or":[{"isActive":True}, {"age":{"$lt":18}}]})

# Find users where age is greater than 30 AND isActive is False.

result = mycollection.find({"age":{"$gt":30}, "isActive":False})

# age is greater than 20 AND (isActive is True OR age is less than 40)

result = mycollection.find({
    "age":{"$gt":20}, 
    "$or":[{"isActive":True}, {"age":{"$lt":40}}]
    })

# Find all users whose age is not 10, 17, or 25.

result = mycollection.find({"age":{"$nin":[10, 17, 25]}})

# Find the user named "Boss" and change their age to 30.

result = mycollection.update_one(
    {"name":"Boss"},
      {"$set":{"age":30}}
      )

# Find "Boss" and remove the isActive field from that document.

result = mycollection.update_one(
    {"name":"Boss"},
    {"$unset":{"isActive":""}}
      )

# Change isActive to False for every user whose age is greater than 40.

result = mycollection.update_many(
    {"age":{"$gt":40}},
    {"$set":{"isActive":False}}
)

# Delete one user whose name is "Boss".

result = mycollection.delete_one({"name":"Boss"})