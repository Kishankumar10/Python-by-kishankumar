from dotenv import load_dotenv
import os
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from datetime import datetime
from bson import ObjectId
from bson.errors import InvalidId


# Database Connection 

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)

db = client["E-commerce-python"]

users = db["users"]
products = db["products"]
orders = db["orders"]


# making email as unique
users.create_index("email", unique=True)


# Format printers

def user_formatter(user=None):

    if user is None:
        print("User not found.\n")

    else:      
        print(f"ID          : {user['_id']}")
        print(f"Name        : {user['name']}")
        print(f"Email       : {user['email']}")
        print(f"Created date: {user['createdAt'].strftime('%d-%m-%Y')}")
        print(f"Mobile      : {user['mobile']}")
        print(f"Address     : {user['address']}\n")


def product_formatter(product=None):
    
    if not product:
        print("product not found.\n")

    else:      
        print(f"ID      : {product['_id']}")
        print(f"Name    : {product['name']}")
        print(f"Price   : {product['price']}")
        print(f"Model   : {product['model']}")
        print(f"Color   : {product['color']}")
        print(f"Stock   : {product['stock']}")
        print(f"Discount: {product['discount']}\n")


def order_formatter(order=None):
    print(f"Order ID     : {order['_id']}")
    print(f"Quantity     : {order['quantity']}")
    print(f"Amount       : {order['amount']}")
    print(f"Paid         : {order['isPaid']}")
    print(f"Ordered Date : {order['orderedDate'].strftime('%d-%m-%Y')}")
    print(f"Delivered    : {order['isDelivered']}\n")


# User function

def sign_up():

    user_data = {
        "name":  input("Enter name: ").strip(),
        "email": input("Enter email: ").strip(),
        "password": input("Enter password: ").strip(),
        "mobile": input("Enter mobile number: ").strip(),
        "address": input("Enter address: ").strip(),
        "createdAt": datetime.now()
    }

    for key,value in user_data.items():
        if not value:
            print(f"{key} cannot be empty")
            return False

    try:
        insert_obj = users.insert_one(user_data)
        print("Sign up successful!.")
        return insert_obj.inserted_id

    except DuplicateKeyError:
        print("Email already in use. Please enter a different email address.")
        return False


def login():

    email = input("Enter email: ").strip()
    password = input("Enter password: ").strip()

    if not email and not password:
        print("Both email and password cannot be empty")
        return False
    elif not email:
        print("Email cannot be empty")
        return False
    elif not password:
        print("Password cannot be empty")
        return False

    user_data = users.find_one({"email": email})

    if user_data and user_data["password"] == password:
        print("login successful")
        return user_data["_id"]
    else:
        print("Invalid Email or Password")
        return False



def get_all_users():

    for user in users.find():
        user_formatter(user)


def get_specific_user_data(user_id):
    try:
        db_id = ObjectId(user_id)
    except InvalidId:
        print("Invalid user ID")
    else:
        user_formatter(users.find_one({"_id": db_id}))   


def update_field(collection, db_id, key, new_value ):  
    collection.update_one(
        {"_id": db_id},
        {"$set": {key: new_value}}      
    )

def update_user_data(user_id):
    
    user = users.find_one({"_id": user_id})
    if not user:
        print("User not found.")
        return

    while True:
        user = users.find_one({"_id": user_id})
        user_formatter(user)
        
        print("\nUpdate menu\n")
        print("1. Name")
        print("2. Email")
        print("3. Password")
        print("4. Mobile")
        print("5. Address")
        print("6. Exit\n")

        try:
            menu = int(input("Enter your menu number: "))
        except ValueError:
            print("Invalid menu number")
            continue

        match menu:

            case 1: # Name

                new_name = input("Enter new name: ").strip()
                if not new_name:
                    print("Name cannot be empty.")
                    continue
                update_field(users, user_id, "name", new_name)
                print("Name was updated successfully!")

            case 2: # Email

                new_email = input("Enter new email: ").strip()
                if not new_email:
                    print("Email cannot be empty.")
                    continue
                try:
                    update_field(users, user_id, "email", new_email)
                    print("Email was updated successfully!")
                except DuplicateKeyError:
                    print("Update failed, Email already exist.")

            case 3: # Password

                old_password = input("Enter your old password: ").strip()

                if old_password == user["password"]:
                    new_password = input("Enter new password: ").strip()
                    if not new_password:
                        print("Password cannot be empty.")
                        continue
                    update_field(users, user_id, "password", new_password)
                    print("Password was updated successfully!")
                else:
                    print("Wrong password")

            case 4: # Mobile

                new_mobile = input("Enter new mobile number: ").strip()
                if not new_mobile:
                    print("Mobile number cannot be empty.")
                    continue
                update_field(users, user_id, "mobile", new_mobile)
                print("Mobile number was updated successfully!")
                
            case 5: # Address

                new_address = input("Enter new address: ").strip()
                if not new_address:
                    print("Address cannot be empty.")
                    continue
                update_field(users, user_id, "address", new_address)
                print("Address was updated successfully!")
                
            case 6: # Exit
                break

            case _:
                print("Invalid menu number")


def delete_user_data(user_id):

    deleted_user = users.find_one_and_delete({"_id": user_id})

    if deleted_user:
        print("Deleted successfully!")
        return True
    else:
        print("ID not found")
        return False
    


# Product functions 

def add_product():

    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty")
        return None 

    try:
        price = float(input("Enter price: "))
        if price <= 0:
            print("Price must be greater than 0")
            return None 
    except ValueError:
        print("Invalid price. Please enter a valid number.")
        return None 

    model = input("Enter model: ").strip()
    if not model:
        print("model cannot be empty")
        return None 

    color = input("Enter color: ").strip()
    if not color:
        print("Color cannot be empty.")
        return None

    try:
        stock = int(input("Enter stock numbers: "))
        if stock < 0:
            print("Stock cannot be negative.")
            return None
    except ValueError:
        print("Invalid stock number. Please enter a whole integer.")
        return None
    try:
        discount = float(input("Enter discount percentage (0-100): "))
        if discount < 0 or discount > 100:
            print("Discount must be between 0 and 100.")
            return None
    except ValueError:
        print("Invalid discount percentage. Please enter a valid number.")
        return None

    product_data = {
        "name": name,
        "price": price,
        "model": model,
        "color": color,
        "stock": stock,
        "discount": discount,
    }

    product_id = products.insert_one(product_data).inserted_id
    print(f"Product added successfully! ID: {product_id}")


def get_all_products():
    for product in products.find():
        product_formatter(product)


def get_specific_product_data():

    product_id = input("Enter your product ID: ")
    try:
        db_id = ObjectId(product_id)
    except InvalidId:
        print("Invalid product ID")
    else:
        product_formatter(products.find_one({"_id": db_id}))


def update_product_data():

    try:
        product_id = ObjectId(input("Enter product ID: "))
    except InvalidId:
        print("Invalid product ID")
        return

    product = products.find_one({"_id": product_id})
    if not product:
        print("Product not found.")
        return

    while True:
        # Refresh product document to reflect latest changes
        product = products.find_one({"_id": product_id})

        product_formatter(product)
        print("\nUpdate menu\n")
        print("1. Name")
        print("2. Price")
        print("3. Model")
        print("4. Color")
        print("5. Stock")
        print("6. Discount")
        print("7. Exit\n")

        try:
            menu = int(input("Enter your menu number: "))
        except ValueError:
            print("Invalid menu number")
            continue

        match menu:

            case 1:  # Name
                new_name = input("Enter new name: ").strip()
                if not new_name:
                    print("Name cannot be empty.")
                    continue

                update_field(products, product_id, "name", new_name)
                print("Product Name was updated successfully!")

            case 2:  # Price
                try:
                    new_price = float(input("Enter new price: "))
                    if new_price <= 0:
                        print("Price must be greater than 0.")
                        continue
                except ValueError:
                    print("Invalid price. Please enter a valid number.")
                    continue

                update_field(products, product_id, "price", new_price)
                print("Product price was updated successfully!")

            case 3:  # Model
                new_model = input("Enter new model: ").strip()
                if not new_model:
                    print("Model cannot be empty.")
                    continue

                update_field(products, product_id, "model", new_model)
                print("Product model was updated successfully!")

            case 4:  # Color
                new_color = input("Enter new color: ").strip()
                if not new_color:
                    print("Color cannot be empty.")
                    continue

                update_field(products, product_id, "color", new_color)
                print("Product color was updated successfully!")

            case 5:  # Stock
                try:
                    new_stock = int(input("Enter new number of stock: "))
                    if new_stock < 0:
                        print("Stock cannot be negative.")
                        continue
                except ValueError:
                    print("Invalid stock number. Please enter a whole integer.")
                    continue

                update_field(products, product_id, "stock", new_stock)
                print("Product stock count was updated successfully!")

            case 6:  # Discount
                try:
                    new_discount = float(
                        input("Enter new discount percentage (0-100): ")
                    )
                    if new_discount < 0 or new_discount > 100:
                        print("Discount must be between 0 and 100.")
                        continue
                except ValueError:
                    print("Invalid discount percentage. Please enter a valid number.")
                    continue

                update_field(products, product_id, "discount", new_discount)
                print("Product discount was updated successfully!")

            case 7:  # Exit
                break

            case _:
                print("Invalid menu number")



def delete_product_data():
    product_id = input("Enter product ID: ")

    try:
        db_id = ObjectId(product_id)
    except InvalidId:
        print("Invalid product ID")
        return None
    else:
        deleted_product  = products.find_one_and_delete({"_id": db_id})

    if deleted_product :
        print("Deleted successfully!")
    else:
        print("ID not found")



# Orders functions

def place_order(user_id):

    try:
        product_id = ObjectId(input("Enter product ID: "))
        
    except InvalidId:
        print("Invalid ID")
        return 
    
    user_data = users.find_one({"_id": user_id})
    product_data = products.find_one({"_id": product_id})

    if not product_data:
        print("Product not found")
        return 
    
    stock = product_data["stock"]

    if stock == 0:
        print("Product out of stock")
        return 
    
    try:
        quantity = int(input("Number of products: "))
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
    except ValueError:
        print("Invalid product number")
        return 
    else:
        if quantity > stock:
            print("Not enough stock")
            return 

    discounted_price = product_data["price"] * (1 - (product_data["discount"] / 100))
    final_price = discounted_price * quantity

    order_data = {
        "userId": user_id,
        "productId": product_id,
        "amount": final_price,
        "isPaid": False,
        "quantity": quantity,
        "orderedDate": datetime.now(),
        "isDelivered": False
    }

    orders.insert_one(order_data)
    products.update_one(
        {"_id": product_id},
        {"$inc":{"stock": -quantity}}
    )
    print("Order placed successfully!\n")

    print("\n=================================================")
    print("                ORDER RECEIPT                    ")
    print("=================================================\n")
    print(f"User name : {user_data['name']}")
    print(f"Product   : {product_data['name']}")
    print(f"Quantity  : {quantity}")
    print(f"Price     : {product_data['price']}")
    print(f"Discount  : {product_data['discount']}%")
    print("\n-------------------------------------------------")
    print(f"Final price: {final_price}")
    print("\n-------------------------------------------------\n")


def get_all_ordered_details():
    cursor = orders.find()
    for order in cursor:
        user = users.find_one({"_id":order["userId"]})
        product = products.find_one({"_id":order["productId"]})
        print("\n=================================================")
        user_formatter(user)
        product_formatter(product)
        order_formatter(order)
        print("\n=================================================")

        
def get_user_orders(user_id):

    cursor = orders.find({"userId": user_id})
    found_any = False
    for order in cursor:
        found_any = True
        product = products.find_one({"_id": order["productId"]})
        product_name = product["name"] if product else "N/A"
        print(f"Product Name : {product_name}")
        order_formatter(order)

    if not found_any:
        print("No orders found for this user.")


def update_delivery_status():
    try:
        order_id = ObjectId(input("Enter order ID: "))
    except InvalidId:
        print("Invalid order ID")
    else:
        is_updated = orders.find_one_and_update(
            {"_id": order_id},
            {"$set": {"isDelivered": True}}
        )
        if is_updated:
            print("Updated successfully")
        else:
            print("Order ID not exist")


# MANAGE ACCOUNT

def manage_account(user_id):

    while True:
        print("\n================================")
        print("         MANAGE ACCOUNT         ")
        print("================================\n")
        print("\t1. View user data")
        print("\t2. Update user data")
        print("\t3. Delete user data")
        print("\t4. Exit")
        print("================================\n")      

        try:
            menu = int(input("Enter your menu number: "))
        except ValueError:
            print("Invalid menu number")
            continue  

        match menu:
            case 1:
                get_specific_user_data(user_id)
            case 2:
                update_user_data(user_id) 
            case 3:
                if delete_user_data(user_id):
                    return True
            case 4:
                break 
            case _:
                print("Menu number not exist")  
    return False  
          

# CUSTOMER MENU 

def customer_menu(user_id):

    while True:

        print("\n================================")
        print("         CUSTOMER MENU          ")
        print("================================\n")
        print("\t1. Manage account")
        print("\t2. View all products")
        print("\t3. View specific products")
        print("\t4. Place order")
        print("\t5. View my orders")
        print("\t6. Log out")
        print("================================\n")

        try:
            menu = int(input("Enter your menu number: "))
        except ValueError:
            print("Invalid menu number")
            continue  

        match menu:
            case 1:
                if manage_account(user_id):
                    return 
            case 2:
                get_all_products() 
            case 3:
                get_specific_product_data()
            case 4:
                place_order(user_id)
            case 5:
                get_user_orders(user_id)
            case 6:
                print("You have been successfully logged out.")
                break 
            case _:
                print("Menu number not exist")      



# PRODUCT MANAGEMENT 

def product_management():
    while True:
        print("\n================================")
        print("      PRODUCT MANAGEMENT        ")
        print("================================\n")
        print("\t1. View all products")
        print("\t2. Add product")
        print("\t3. Update product data")
        print("\t4. Delete product")
        print("\t5. Exit")
        print("================================\n")

        try:
            menu = int(input("Enter your menu number: "))
        except ValueError:
            print("Invalid menu number")
            continue

        match menu:
            case 1:
                get_all_products()
            case 2:
                add_product()
            case 3:
                update_product_data()
            case 4:
                delete_product_data()
            case 5:
                break
            case _:
                print("Menu number not exist")  


# ORDER MANAGEMENT

def order_management():
    while True:
        print("\n================================")
        print("       ORDER MANAGEMENT         ")
        print("================================\n")
        print("\t1. View all orders")
        print("\t2. Update delivery status")
        print("\t3. Exit")
        print("================================\n")

        try:
            menu = int(input("Enter your menu number: "))
        except ValueError:
            print("Invalid menu number")
            continue

        match menu:
            case 1:
                get_all_ordered_details()
            case 2:
                update_delivery_status()
            case 3:
                break
            case _:
                print("Menu number not exist")


# MANAGEMENT CONSOLE

def management_console():
    while True:
        print("\n================================")
        print("      MANAGEMENT CONSOLE        ")
        print("================================\n")
        print("\t1. Get all users")
        print("\t2. Manage Products")
        print("\t3. Manage orders")
        print("\t4. Exit")
        print("================================\n")

        try:
            menu = int(input("Enter your menu number: "))
        except ValueError:
            print("Invalid menu number")
            continue  

        match menu:
            case 1:
                get_all_users() 
            case 2:
                product_management()
            case 3:
                order_management()
            case 4:
                break
            case _:
                print("Menu number not exist") 

    
# MAIN MENU

while True:

    print("\n================================")
    print("           MAIN MENU            ")
    print("================================\n")
    print("\t1. Sign Up")
    print("\t2. Login")
    print("\t3. Management console")
    print("\t4. Exit")
    print("================================\n")

    try:
        menu = int(input("Enter your menu number: "))
    except ValueError:
        print("Invalid menu number")
        continue

    match menu:
        case 1:
            user_id = sign_up()
            if  user_id:
                customer_menu(user_id)
        case 2:
            user_id = login()
            if user_id:
                customer_menu(user_id) 
        case 3:
            management_console()     
        case 4:
            print("program finished")
            break
        case _:
            print("Menu number not exist")