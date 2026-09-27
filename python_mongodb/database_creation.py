from pymongo import MongoClient
from bson import ObjectId


mongo_url = MongoClient("mongodb+srv://Kishankumar:200910@cluster0.vq7585o.mongodb.net/?appName=Cluster0")
my_db = mongo_url["Kishan_db"]
my_collection = my_db["users_data"]
product_collection = my_db["product"]

student_data = {
    "name": "Kishankumar",
    "email": "kishan@gmail.com",
    "mobile": 9589038938,
    "marks": 84,
    "address": "A-14, aaa street, puducherry",
    "isActive": True
}

def create_user(user):
    data = my_collection.insert_one(user)
    print(data)
    print("User inseted successfully!")

# create_user(student_data)

multiple_user_data = [
    {
        "name": "Raju Vasala",
        "email": "vasala@gmail.com",
        "mobile": 9635278521,
        "marks": 56,
        "address": "A-2, bbb street",
        "isActive": False
    },
    {
        "name": "Addanki Varun",
        "email": "addanki@gmail.com",
        "mobile": 9583645127,
        "marks": 99,
        "address": "D-87, ccc street",
        "isActive": True
    },
    {
        "name": "Banu Kothari",
        "email": "kothari@gmail.com",
        "mobile": 9237456981,
        "marks": 45,
        "address": "B-4, ddd street",
        "isActive": True
    }
]

def add_multiple_user(users):
    my_collection.insert_many(users)
    print("Inserted successfully!")

# add_multiple_user(multiple_user_data)


# Get all users

def get_all_users():
    users_data = my_collection.find()
    for i in users_data:
        print(i)

# get_all_users()


# Get specific users

def get_specific_users(user_id):
    user = my_collection.find_one({"_id": ObjectId(user_id)})
    print(user)

# get_specific_users("6ab3f750383bb388b186ae09")

def delete_user(user_id):
    user_delete = my_collection.delete_one({"_id": ObjectId(user_id)})
    print("User deleted successfully!")

# delete_user("6ab3f751383bb388b186ae0c")


# Update key value pairs 

def update_data(user_id):
    my_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"isActive": False}}
    )
    print("Updated successfully!")

# update_data("6ab3f751383bb388b186ae0b")


products_data = [
    {
        "name": "Office Chair",
        "price": 2000,
        "model": "Standard Ergonomic",
        "color": "Black",
        "stock": 25,
        "discount": 10
    },
    {
        "name": "Computer Monitor",
        "price": 60000,
        "model": "24-Inch oled",
        "color": "White",
        "stock": 15,
        "discount": 15
    },
    {
        "name": "Smart TV",
        "price": 100000,
        "model": "50-Inch 4K",
        "color": "Black",
        "stock": 10,
        "discount": 20
    },
    {
        "name": "Gaming Laptop",
        "price": 85000,
        "model": "Pro Series",
        "color": "Dark Gray",
        "stock": 8,
        "discount": 12
    },
    {
        "name": "Smartphone",
        "price": 60000,
        "model": "S26 ultra",
        "color": "Silver",
        "stock": 30,
        "discount": 10
    },
    {
        "name": "GAN 12 maglev",
        "price": 7000,
        "model": "3x3 Magnetic",
        "color": "Stickerless",
        "stock": 50,
        "discount": 5
    },
    {
        "name": "Wireless Mouse",
        "price": 2500,
        "model": "Silent Click",
        "color": "Gray",
        "stock": 40,
        "discount": 10
    },
    {
        "name": "Desk Lamp",
        "price": 3000,
        "model": "smart lamp",
        "color": "Warm White",
        "stock": 20,
        "discount": 15
    },
    {
        "name": "Backpack",
        "price": 4500,
        "model": "Travel Slim",
        "color": "Blue",
        "stock": 35,
        "discount": 20
    },
    {
        "name": "Water Bottle",
        "price": 1200,
        "model": "Steel Insulated",
        "color": "Red",
        "stock": 60,
        "discount": 10
    }
]

def insert_products(products_records):
    product_collection.insert_many(products_records)
    print("Product added successfully!")

# insert_products(products_data)