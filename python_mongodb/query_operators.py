from pymongo import MongoClient


mongo_url = MongoClient("mongodb+srv://Kishankumar:200910@cluster0.vq7585o.mongodb.net/?appName=Cluster0")
my_db = mongo_url["Kishan_db"]
my_collection = my_db["users_data"]
product_collection = my_db["product"]


def sort_data():
    data = product_collection.find().sort("name", -1)
    for i in data:
        print(i,"\n")
# sort_data()


# Equality
def fun_1():
    data_1 = my_collection.find({"isActive": True})
    for i in data_1:
        print(i)
# fun_1()


# Less Than
def fun_2():
    data_2 = product_collection.find({"price": {"$lt": 60000}})
    for i in data_2:
        print(i)
# fun_2()


# Greater Than
def fun_3():
    data_3 = product_collection.find({"price": {"$gt": 60000}})
    for i in data_3:
        print(i)
# fun_3()


# Less Than Equal to
def fun_4():
    data_4 = product_collection.find({"price": {"$lte": 60000}})
    for i in data_4:
        print(i)
# fun_4()


# Greater Than Equal to
def fun_5():
    data_5 = product_collection.find({"price": {"$gte": 60000}})
    for i in data_5:
        print(i)
# fun_5()


# Not Equal to
def fun_6():
    data_6 = my_collection.find({"isActive": {"$ne": True}})
    for i in data_6:
        print(i)
# fun_6()


# Logical AND
def fun_7():
    data_7 = my_collection.find({"$and": [{"isActive": {"$ne": False}}, {"marks": {"$lte": 60}}]})
    for i in data_7:
        print(i)
# fun_7()


# Logical OR
def fun_8():
    data_8 = my_collection.find({"$or": [{"isActive": {"$ne": True}}, {"marks": {"$lte": 60}}]})
    for i in data_8:
        print(i)
# fun_8()


# Logical NOT
def fun_9():
    data_9 = my_collection.find({"marks":{"$not": {"$lt": 60}}})
    for i in data_9:
        print(i)
# fun_9()