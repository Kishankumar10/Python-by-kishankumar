from pymongo import MongoClient
from dotenv import load_dotenv
import os 
from datetime import datetime

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["Movie_DB"]

movies = db["movies"]
bookings = db["bookings"]

movies.create_index("movie_id", unique=True)
bookings.create_index("booking_id", unique=True)

show_time_slots = {
    1: "10:00",
    2: "13:00",
    3: "16:00",
    4: "19:00",
    5: "22:00"
}

# Input validation function 

def get_input(prompt):
    while True:
        value = input(prompt).strip()
        if not value:
            print("❌ Input cannot be empty, Try again\n")
            continue
        return value

def get_positive_int(prompt):
    while True: 
        try:
            value = int(get_input(prompt))
            if value <= 0:
                print("❌ Value must be greater than 0\n")
                continue
            return value
        except ValueError:
            print("❌ Invalid input, Enter a valid integer\n")

def get_positive_float(prompt):
    while True: 
        try:
            value = float(get_input(prompt))
            if value <= 0:
                print("❌ Value must be greater than 0\n")
                continue
            return value
        except ValueError:
            print("❌ Invalid input, Enter a valid number\n")

def get_date(prompt):
    while True:
        try: 
            value = datetime.strptime(get_input(prompt), "%d/%m/%Y")
            return value
        except ValueError:
            print("❌ The format is Invalid, Try again\n")

def get_unique_id(prompt, collection, id_field):
    while True:
        value = get_input(prompt)
        if collection.find_one({id_field: value}):
            print("❌ ID already exists. Try again with a different ID.\n")
            continue
        return value

def get_existing_document(prompt, collection, id_field):
    while True:
        value = get_input(prompt)
        document = collection.find_one({id_field: value})

        if document:
            return document

        print("🔍 ID not found. Try again.")

def get_show_time():
    print("\n⏰ TIME SLOTS\n")

    for number, time in show_time_slots.items():
        print(f"Slot-{number} : {time}")
    print()

    while True:
        slot = get_positive_int("Enter time slot number (1-5): ")

        if slot in show_time_slots:
            return show_time_slots[slot]

        print("❌ Invalid slot number.")

def get_show_date(movie):  
    while True:
        show_date = get_date("Enter show date (dd/mm/yyyy): ")
        if show_date.date() < movie['release_date'].date():
            print(f"📅 Entered date is before the release date({movie['release_date'].strftime('%d-%m-%Y')}), Try again\n")
            continue
        if show_date.date() < datetime.now().date():
            print("❌ You cannot book movie in past\n")
            continue
        return show_date  

    
# Printer formatter function 

def movie_formatter(movie):

    if not movie:
        print("❌ Movie not found\n")
        return 

    print(f"Movie ID     : {movie['movie_id']}")
    print(f"Movie name   : {movie['movie_name']}")
    print(f"Language     : {movie['language']}")
    print(f"Genre        : {movie['genre']}")
    print(f"Duration     : {movie['duration']} minutes")
    print(f"Release Date : {movie['release_date'].strftime('%d-%m-%Y')}")
    print(f"Price        : ₹{movie['price']}\n")

def booking_formatter(booking):
    if not booking:
        print("❌ Booking not found\n")
        return
    
    print(f"Booking ID    : {booking['booking_id']}")
    print(f"Customer name : {booking['customer_name']}")
    print(f"Phone number  : {booking['phone_number']}")
    print(f"Movie ID      : {booking['movie_id']}")
    print(f"Movie name    : {booking['movie_name']}")
    print(f"Show date     : {booking['show_date'].strftime('%d-%m-%Y')}")
    print(f"Show time     : {booking['show_time']}")
    print(f"Ticket price  : ₹{booking['ticket_price']}")
    print(f"Tickets       : {booking['tickets']}")
    print(f"Total amount  : ₹{booking['total_amount']}\n")

def display_compact_movie_list():
    movie_list = list(movies.find())
    if not movie_list:
        print("📽️ ❌ Oops! No movies available")
        return False
    print(f"\n{'-'*50}\n  ID  | PRICE |  MOVIE NAME\n{'-'*50}")
    for doc in movie_list:
        print(f" {doc['movie_id']} | ₹{doc['price']} | {doc['movie_name']}")
    print('-'*50)
    return True


# Helper function

def update_field(collection, filter_data, field, value):
    collection.update_one(
        filter_data,
        {"$set": {field: value}}
    )

def get_confirmation(prompt):
    while True:
        value = get_input(prompt).lower()

        if value == "y":
            return True
        elif value == "n":
            return False

        print("❌ Please enter y or n.")


# MOVIE FUNCTIONS

def add_movie():
    movie_id = get_unique_id("Enter movie ID: ", movies, "movie_id")
    movie_name = get_input("Enter movie name: ")
    language = get_input("Enter movie language: ")
    genre = get_input("Enter movie genre: ")
    duration = get_positive_int("Enter the duration in minutes: ")
    release_date = get_date("Enter release date (format: dd/mm/yyyy): ")
    price = get_positive_float("Enter Price: ")

    movie_data = {
        "movie_id": movie_id,
        "movie_name": movie_name,
        "language": language,
        "genre": genre,
        "duration": duration,
        "release_date": release_date,
        "price": price
    }
    movies.insert_one(movie_data)
    print("✅ Movie added successfully!")

def view_all_movies():

    cursor = movies.find()
    has_movie = False

    for movie in cursor:
        has_movie = True
        movie_formatter(movie)

    if not has_movie:
        print("❌ No movies found")

def search_movie():

    print("What field you are going to use to search movie\n")
    print("1. Movie ID")
    print("2. Movie name\n")

    menu = get_input("Enter menu number: ")
    match menu:
        case "1":
            movie_id = get_input("Enter Movie ID: ")
            movie = movies.find_one({"movie_id": movie_id})
            print()
            movie_formatter(movie)
        case "2":
            movie_name = get_input("Enter movie name: ")
            movie = movies.find_one({"movie_name": movie_name})
            movie_formatter(movie)
        case _:
            print("❌ Invalid menu number")


def update_movie_details():
    if not display_compact_movie_list():
        return 
    movie = get_existing_document("Enter Movie ID: ", movies, "movie_id" )
    movie_id = movie["movie_id"]
    filter_data = {"movie_id": movie_id}
    while True:
        movie = movies.find_one({"movie_id": movie_id})
        print()
        movie_formatter(movie)
        
        print("UPDATE MOVIE\n")

        print("1. Movie Name")
        print("2. Language")
        print("3. Genre")
        print("4. Duration")
        print("5. Release Date")
        print("6. Price")
        print("7. Exit\n")

        menu = get_input("Enter menu number: ")

        match menu:
            case "1":
                name = get_input("Enter new movie name: ")
                update_field(movies, filter_data, "movie_name", name)
                print("✅ Movie name updated!")
            case "2":
                language = get_input("Enter new language: ")
                update_field(movies, filter_data, "language", language)
                print("✅ Language updated!")
            case "3":
                genre = get_input("Enter new genre: ")
                update_field(movies, filter_data, "genre", genre)
                print("✅ Genre updated!")
            case "4":
                duration = get_positive_int("Enter new duration (mins): ")
                update_field(movies, filter_data, "duration", duration)
                print("✅ Duration updated!")
            case "5":
                release_date = get_date("Enter new release date (dd/mm/yyyy): ")
                update_field(movies, filter_data, "release_date", release_date)
                print("✅ Release date updated!")
            case "6":
                price = get_positive_float("Enter new price: ")
                update_field(movies, filter_data, "price", price)
                print("✅ Price updated!")
            case "7":
                print("➡️  Exited update menu.")
                break 
            case _:
                print("❌ Invalid menu number")


def delete_movie():
    movie_id = get_input("Enter Movie ID: ")
    movie = movies.find_one({"movie_id": movie_id})

    if not movie:
        print("🔍 Movie ID not found.")
        return
    
    print("\n🎬 --- MOVIE TO DELETE ---\n")
    movie_formatter(movie)

    confirm = get_confirmation("\n⚠️  Are you sure you want to permanently delete this movie? (y/n):")
    if confirm :
        movies.delete_one({"movie_id": movie_id})
        print("🗑️  Movie deleted successfully!")
    else:
        print("ℹ️  Deletion canceled.")


# BOOKING FUNCTIONS     

def create_booking():

    if not display_compact_movie_list():
        return 
    
    booking_id = get_unique_id("Enter Booking ID: ", bookings, "booking_id")
    customer_name = get_input("Enter your name: ")
    phone_number = get_input("Enter your mobile number: ")
    movie = get_existing_document("\nEnter Movie ID: ", movies, "movie_id")
    show_date = get_show_date(movie)
    show_time = get_show_time()
    tickets  = get_positive_int("Enter a number of tickets you want: ")
    total_amount = round(tickets  * movie["price"], 2)

    booking_data = {
        "booking_id": booking_id,
        "customer_name": customer_name,
        "phone_number": phone_number,
        "movie_id": movie["movie_id"],
        "movie_name": movie["movie_name"],
        "show_date": show_date,
        "show_time": show_time,
        "ticket_price": movie["price"],
        "tickets": tickets,
        "total_amount": total_amount
    }

    print("\n  BOOKING PREVIEW\n")
    booking_formatter(booking_data)

    confirm = get_confirmation("\n🎬 Are you sure you want to book this movie❓(y/n):")

    if confirm:
        bookings.insert_one(booking_data)
        print("✅ 🎉🎉🎉 Ticket booked successfully!")
    else:
        print("❌🎟️  Booking cancelled.")

def view_all_bookings():

    cursor = bookings.find()
    has_booking = False

    for booking in cursor:
        has_booking = True
        booking_formatter(booking)

    if not has_booking:
        print("🔍❌ No booking found")

def search_booking():
    booking_id = get_input("Enter Booking ID: ")
    booking = bookings.find_one({"booking_id": booking_id})
    print()
    booking_formatter(booking)

def update_booking():

    if not bookings.find_one():
        print("❌ No bookings available to update.")
        return
    
    booking = get_existing_document("Enter Booking ID: ", bookings, "booking_id")
    booking_id = booking["booking_id"]
    filter_data = {"booking_id": booking_id }

    while True:
        booking = bookings.find_one({"booking_id": booking_id})
        print()
        booking_formatter(booking)

        print("UPDATE BOOKING\n")
        print("1. Customer name")
        print("2. Phone number")
        print("3. Show date")
        print("4. Show time")
        print("5. Number of tickets")
        print("6. Exit\n")

        menu = get_input("Enter menu number: ")

        match menu:
            case "1":
                name = get_input("Enter customer name: ")
                update_field(bookings, filter_data, "customer_name", name)
                print("\n✅ Customer name updated successfully!")
            case "2":
                phone = get_input("Enter new mobile number: ")
                update_field(bookings, filter_data, "phone_number", phone)
                print("\n✅ Phone number updated successfully!")
            case "3":
                movie = movies.find_one({"movie_id": booking["movie_id"]})
                if not movie:
                    print("\n❌ Associated movie no longer exists in database.")
                    continue
                show_date = get_show_date(movie)
                update_field(bookings, filter_data, "show_date", show_date)
                print("\n✅ Show date is updated successfully!")
            case "4":
                show_time = get_show_time()
                update_field(bookings, filter_data, "show_time", show_time)
                print("\n✅ Show time is updated successfully!")
            case "5":
                tickets = get_positive_int("Enter a number of tickets you want: ")
                total_amount = round(tickets  * booking["ticket_price"], 2)
                bookings.update_one(filter_data, {"$set": {"tickets": tickets, "total_amount": total_amount}})
                print(f"\n✅ Tickets updated successfully! New total: ₹{total_amount}")
            case "6":
                print("\n➡️  Exited update menu.")
                break
            case _:
                print("\n❌ Invalid menu number")

def cancel_booking():
    booking_id = get_input("Enter Booking ID: ")
    booking = bookings.find_one({"booking_id": booking_id})

    if not booking:
        print("🔍 Booking ID not found.")
        return

    print("\n🎟️ --- BOOKING TO CANCEL ---\n")
    booking_formatter(booking)

    confirm = get_confirmation("\n⚠️ Are you sure you want to cancel this booking? (y/n): ")
    if confirm:
        bookings.delete_one({"booking_id": booking_id})
        print("🗑️ Booking canceled successfully!")
    else:
        print("ℹ️ Cancellation process aborted.")

def movie_management():

    while True:

        print("\n======================================")
        print("           MOVIE MANAGEMENT           ")
        print("======================================\n")
        print("\t1. Add movie")
        print("\t2. View all movies")
        print("\t3. Search movie")
        print("\t4. Update movie details")
        print("\t5. Delete a movie record")
        print("\t6. Exit")
        print("======================================\n")

        menu = get_input("Enter menu number: ")

        match menu:
            case "1":
                add_movie()
            case "2":
                view_all_movies()
            case "3":
                search_movie()
            case "4":
                update_movie_details()
            case "5":
                delete_movie()
            case "6":
                print("➡️  Exited movie menu.")
                break
            case _:
                print("❌ Invalid menu number")

def booking_management():

    while True:

        print("\n======================================")
        print("          BOOKING MANAGEMENT          ")
        print("======================================\n")
        print("\t1. Create booking")
        print("\t2. View all bookings")
        print("\t3. Search booking")
        print("\t4. Update booking")
        print("\t5. Cancel booking")
        print("\t6. Exit")
        print("======================================\n")

        menu = get_input("Enter menu number: ")

        match menu:
            case "1":
                create_booking()
            case "2":
                view_all_bookings()
            case "3":
                search_booking()
            case "4":
                update_booking()
            case "5":
                cancel_booking()
            case "6":
                print("➡️  Exited booking menu.")
                break
            case _:
                print("❌ Invalid menu number")

while True:

    print("\n======================================")
    print("      MOVIE TICKET BOOKING SYSTEM     ")
    print("======================================\n")
    print("\t1. Movie Management")
    print("\t2. Booking Management")
    print("\t3. Exit")
    print("======================================\n")

    menu = get_input("Enter menu number: ")

    match menu:
        case "1":
            movie_management()
        case "2":
            booking_management()
        case "3":
            print("\n😃 Thank you for using the Movie Ticket Booking System!")
            break
        case _:
            print("❌ Invalid menu number")