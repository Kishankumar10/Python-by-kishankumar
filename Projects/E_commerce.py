from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from pymongo.errors import DuplicateKeyError
from bson.errors import InvalidId


# Connection to database

mongo_URL = MongoClient("mongodb+srv://<username>:<password>@cluster0.vq7585o.mongodb.net/?appName=Cluster0")

my_db = mongo_URL["E-commerce"]

users = my_db["users"]
products = my_db["products"]
orders = my_db["orders"]

# making email as unique
users.create_index("email", unique=True)


# Formatters

def user_formatter(user):

    if not user:
        print("User not found.\n")
        return 

    print(f"\nID           : {user['_id']}")
    print(f"Name         : {user['name']}")
    print(f"Email        : {user['email']}")
    print(f"Created date : {user['createdAt'].strftime('%d-%m-%Y')}")
    print(f"Mobile       : {user['mobile']}")
    print(f"Address      : {user['address']}\n")


def product_formatter(product):

    if not product:
        print("Product not found.\n")
        return 
    
    print(f"\nID       : {product['_id']}")
    print(f"Name     : {product['name']}")
    print(f"Price    : {product['price']}")
    print(f"Model    : {product['model']}")
    print(f"Color    : {product['color']}")
    print(f"Stock    : {product['stock']}")
    print(f"Discount : {product['discount']}\n")


def order_formatter(order):

    if not order:
        print("Order not found.")
        return 

    print(f"\nOrder ID     : {order['_id']}")
    print(f"Quantity     : {order['quantity']}")
    print(f"Amount       : {order['amount']}")
    print(f"Paid         : {order['isPaid']}")
    print(f"Ordered Date : {order['orderedDate'].strftime('%d-%m-%Y')}")
    print(f"Delivered    : {order['isDelivered']}\n")


# Users function 

def add_users():
    user_data = {
        "name":  input("\nEnter name: ").strip(),
        "email": input("Enter email: ").strip(),
        "password": input("Enter password: ").strip(),
        "mobile": input("Enter mobile number: ").strip(),
        "address": input("Enter address: ").strip(),
        "createdAt": datetime.now()
    }

    for key,value in user_data.items():
        if not value:
            print(f"\n{key} cannot be empty")
            return

    try:
        users.insert_one(user_data)
        print("\nSign up successful!.")
    except DuplicateKeyError:
        print("\nEmail already exist. Please enter a different email address.")


def check_email_and_password():

    email = input("\nEnter email: ").strip()
    password = input("Enter password: ").strip()

    if not email and not password:
        print("Both email and password cannot be empty")
        return 
    elif not email:
        print("Email cannot be empty")
        return 
    elif not password:
        print("Password cannot be empty")
        return 

    user_data = users.find_one({"email": email})

    if user_data and user_data["password"] == password:
        print("login successful")
    
    else:
        print("Invalid Email or Password")


def get_all_users():
    users_cursor = users.find()
    has_users = False
    
    for user in users_cursor:
        has_users = True
        user_formatter(user)

    if not has_users:
        print("\nNo users found")


def get_specific_user_data():
    
    try:
        user_id = ObjectId(input("Enter User ID: ").strip())
    except InvalidId:
        print("Invalid user ID")
    else:
        user_formatter(users.find_one({"_id": user_id}))   


def update_field(collection, db_id, key, new_value ):  
    collection.update_one(
        {"_id": db_id},
        {"$set": {key: new_value}}      
    )


def update_user_data():
    
    try:
        user_id = ObjectId(input("Enter User ID: ").strip())
    except InvalidId:
        print("Invalid user ID")  
        return   

    user = users.find_one({"_id": user_id})
    if not user:
        print("User not found.")
        return

    while True:
        user = users.find_one({"_id": user_id})
        user_formatter(user)
        
        print("Update menu")
        print("1. Name")
        print("2. Email")
        print("3. Password")
        print("4. Mobile")
        print("5. Address")
        print("6. Exit")

        try:
            menu = int(input("Enter your menu number: "))
        except ValueError:
            print("Enter only integers")
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


def delete_user_data():

    try:
        user_id = ObjectId(input("Enter your ID: ").strip())
    except InvalidId:
        print("Invalid user ID")
        return None
    else:
        deleted_user  = users.find_one_and_delete({"_id": user_id})

    if deleted_user :
        print("Deleted successfully!")
    else:
        print("ID not found")

# User menu 
def user_menu():

    while True:

        print("\n======================================")
        print("             USERS MENU               ")
        print("======================================\n")
        print("\t1. Add user")
        print("\t2. Login")
        print("\t3. Get all users")
        print("\t4. Get specific user")
        print("\t5. Update user data")
        print("\t6. Delete user data")
        print("\t7. Exit")
        print("======================================\n")

        try:
            menu = int(input("Enter your menu number: "))
        except ValueError:
            print("Enter only integers")
            continue

        match menu:

            case 1: 
                add_users()
            case 2: 
                check_email_and_password()
            case 3: 
                get_all_users()
            case 4: 
                get_specific_user_data()
            case 5: 
                update_user_data()
            case 6: 
                delete_user_data()
            case 7: 
                break
            case _:
                print("Invalid menu number")   



# Product functions 

def add_product():
    
    name = input("\nName: ").strip()
    if not name:
        print("\nName cannot be empty")
        return 

    model = input("Model: ").strip()
    if not model:
        print("\nModel cannot be empty")
        return 

    color = input("Color: ").strip()
    if not color:
        print("\nColor cannot be empty")
        return 

    try:
        price = float(input("Price: ").strip())
        if price < 0:
            print("\nPrice must be greater than 0.")
            return
    except ValueError:
        print("\nInvalid price! Must be a number.")
        return

    try:
        stock = int(input("Stock: ").strip())
        if stock < 0:
            print("\nStock cannot be negative.")
            return
    except ValueError:
        print("\nInvalid stock! Must be a whole number.")
        return

    try:
        discount = float(input("Discount percentage: ").strip())
        if discount < 0 or discount > 100:
            print("\nDiscount must be between 0 and 100.")
            return
    except ValueError:
        print("\nInvalid discount! Must be a number.")
        return

    product_data = {
        "name": name,
        "price": price,
        "model": model,
        "color": color,
        "stock": stock,
        "discount": discount,
    }

    products.insert_one(product_data)
    print("\nProduct added successfully!")


def get_all_products():
    products_cursor = products.find()
    has_products = False

    for product in products_cursor:
        has_products = True
        product_formatter(product)

    if not has_products:
        print("\nNo products found")


def get_specific_product_data():

    try:
        product_id = ObjectId(input("Enter your product ID: ").strip())
    except InvalidId:
        print("Invalid product ID")
    else:
        product_formatter(products.find_one({"_id": product_id}))


def update_product_data():

    try:
        product_id = ObjectId(input("\nEnter product ID: ").strip())
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
        print("UPDATE MENU\n")
        print("1. Name")
        print("2. Price")
        print("3. Model")
        print("4. Color")
        print("5. Stock")
        print("6. Discount")
        print("7. Exit")

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
                    if new_price < 0:
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

    try:
        product_id = ObjectId(input("Enter product ID: ").strip())
    except InvalidId:
        print("Invalid product ID")
        return 
    else:
        deleted_product  = products.find_one_and_delete({"_id": product_id})

    if deleted_product :
        print("Deleted successfully!")
    else:
        print("ID not found")


def product_menu():

    while True:

        print("\n======================================")
        print("            PRODUCTS MENU             ")
        print("======================================\n")
        print("\t1. Add product")
        print("\t2. Get all products")
        print("\t3. Get specific product")
        print("\t4. Update product data")
        print("\t5. Delete product data")
        print("\t6. Exit")
        print("======================================\n")

        try:
            menu = int(input("Enter your menu number: "))
        except ValueError:
            print("Enter only integers")
            continue

        match menu:

            case 1:
                add_product()
            case 2:
                get_all_products()
            case 3:
                get_specific_product_data()
            case 4:
                update_product_data()
            case 5:
                delete_product_data()
            case 6:
                break
            case _:
                print("Invalid menu number")


# Orders functions

def place_order():

    try:
        user_id = ObjectId(input("\nEnter user ID: ").strip())
        product_id = ObjectId(input("Enter product ID: ").strip())
        
    except InvalidId:
        print("\nInvalid ID")
        return 
    
    user_data = users.find_one({"_id": user_id})
    product_data = products.find_one({"_id": product_id})

    if not user_data:
        print("\nUser not found")
        return 

    if not product_data:
        print("\nProduct not found")
        return 
    
    stock = product_data["stock"]

    if stock == 0:
        print("\nProduct out of stock")
        return 
    try: 
        quantity = int(input("Number of products: "))
    except ValueError:
        print("\nQuantity must be a integer")
        return 

    if quantity < 1:
        print("\nQuantity must be at least 1")
        return 
    
    if quantity > stock:
        print("\nNot enough stock")
        return 

    discounted_price = product_data["price"] * (1 - (product_data["discount"] / 100))
    final_price = round(discounted_price * quantity, 2)

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
        {"$set":{"stock": stock - quantity}}
    )
    print("\nOrder placed successfully!")

    print("\n======================================")
    print("            ORDER RECEIPT             ")
    print("======================================")
    print(f"User name   : {user_data['name']}")
    print(f"Product     : {product_data['name']}")
    print(f"Quantity    : {quantity}")
    print(f"Price       : {product_data['price']}")
    print(f"Discount    : {product_data['discount']}%")
    print("--------------------------------------")
    print(f"Final price : {final_price}")
    print("--------------------------------------\n")

def get_all_order_details():
    orders_cursor = orders.find()
    has_orders = False

    for order in orders_cursor:
        has_orders = True
        user = users.find_one({"_id": order["userId"]})
        product = products.find_one({"_id": order["productId"]})

        print("======================================")
        user_formatter(user)
        product_formatter(product)
        order_formatter(order)
        print("======================================")

    if not has_orders:
        print("\nNo orders found")


def get_user_orders():

    try:
        user_id = ObjectId(input("\nEnter user ID: ").strip())
    except InvalidId:
        print("\nInvalid user ID")
        return

    orders_cursor = orders.find({"userId": user_id})
    has_orders = False

    for order in orders_cursor:
        has_orders = True
        product = products.find_one({"_id": order["productId"]})

        if product:
            product_name = product["name"]
        else:
            product_name = "Product Deleted"

        print(f"\nProduct Name : {product_name}")
        order_formatter(order)

    if not has_orders:
        print("\nNo orders found for this user.")


def update_delivery_status():

    try:
        order_id = ObjectId(input("\nEnter order ID: ").strip())
    except InvalidId:
        print("\nInvalid order ID")
        return

    is_updated = orders.find_one_and_update(
        {"_id": order_id},
        {"$set": {"isDelivered": True, "isPaid": True}}
    )

    if is_updated:
        print("\nDelivery and payment status updated successfully!")
    else:
        print("\nOrder ID does not exist")


def order_menu():

    while True:

        print("\n======================================")
        print("              ORDER MENU              ")
        print("======================================\n")
        print("\t1. Place order")
        print("\t2. Get all order details")
        print("\t3. Get user orders")
        print("\t4. Update delivery status")
        print("\t5. Exit")
        print("======================================\n")

        try:
            menu = int(input("Enter your menu number: "))
        except ValueError:
            print("Enter only integers")
            continue

        match menu:

            case 1:
                place_order()
            case 2:
                get_all_order_details()
            case 3:
                get_user_orders()
            case 4:
                update_delivery_status()
            case 5:
                break
            case _:
                print("Invalid menu number")


# MAIN MENU

while True:

    print("\n======================================")
    print("              MAIN MENU               ")
    print("======================================\n")
    print("\t1. User Management")
    print("\t2. Product Management")
    print("\t3. Order Management")
    print("\t4. Exit")
    print("======================================\n")

    try:
        choice = int(input("Enter your menu number: "))
    except ValueError:
        print("Enter only integers")
        continue

    match choice:

        case 1:
            user_menu()
        case 2:
            product_menu()
        case 3:
            order_menu()
        case 4:
            print("\nThank you for using our website. Goodbye!\n")
            break
        case _:
            print("Invalid menu number")