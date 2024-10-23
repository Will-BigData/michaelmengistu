from auth import sign_up, login, view_all_users, promote_to_admin, delete_user
from crud import add_book, view_books, delete_book, create_order, update_book, view_order_history
import logging

current_user = None

def main_menu():
    while True:
        print("\nWelcome to the Bookstore!")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            handle_sign_up()
        elif choice == '2':
            handle_login()
        elif choice == '3':
            print("Thank you for visiting!")
            break
        else:
            print("Invalid option. Please try again.")

def handle_sign_up():
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")
    sign_up(username, password, email)

def handle_login():
    global current_user
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = login(username, password)
    if user:
        current_user = user
        if user['role'] == 'admin':
            admin_menu()
        else:
            user_menu()

def user_menu():
    while True:
        print("\nUser Menu")
        print("1. View Books")
        print("2. Purchase a Book")
        print("3. View Order History")
        print("4. Log Out")
        choice = input("Select an option: ")

        if choice == '1':
            books = view_books()
            for book in books:
                print(f"{book['book_id']}: {book['title']} by {book['author']} - ${book['price']}, stock_quantity: {book['stock_quantity']}")
        elif choice == '2':
            handle_purchase()
        elif choice == '3':
            handle_view_orders()
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")

def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. View Books")
        print("2. Add a Book")
        print("3. Delete a Book")
        print("4. Manage Users")
        print("5. Log Out")
        choice = input("Select an option: ")

        if choice == '1':
            books = view_books()
            for book in books:
                print(f"{book['book_id']}: {book['title']} by {book['author']} - ${book['price']}")
        elif choice == '2':
            handle_add_book()
        elif choice == '3':
            handle_delete_book()
        elif choice == '4':
            handle_manage_users()
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")

def handle_add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    price = float(input("Enter price: "))
    stock_quantity = int(input("Enter stock quantity: "))
    publication_date = input("Enter publication date (YYYY-MM-DD): ")
    add_book(title, author, genre, price, stock_quantity, publication_date)

def handle_delete_book():
    book_id = int(input("Enter the book ID to delete: "))
    delete_book(book_id)

def handle_purchase():
    book_id = int(input("Enter the book ID to purchase: "))
    quantity = int(input("Enter quantity: "))
    create_order(current_user['user_id'], book_id, quantity)

def handle_view_orders():
    orders = view_order_history(current_user['user_id'])
    if orders:
        print("\nOrder History:")
        for order in orders:
            print(f"Order ID: {order['order_id']}, Book: {order['title']}, Quantity: {order['quantity']}, "
                  f"Total Price: ${order['total_price']}, Status: {order['status']}, Date: {order['created_at']}")
    else:
        print("No orders found.")

def handle_manage_users():
    while True:
        print("\nManage Users")
        print("1. View All Users")
        print("2. Promote User to Admin")
        print("3. Delete User")
        print("4. Back to Admin Menu")
        choice = input("Select an option: ")

        if choice == '1':
            users = view_all_users()
            for user in users:
                print(f"{user['user_id']}: {user['username']} ({user['role']}) - {user['email']}")
        elif choice == '2':
            user_id = int(input("Enter the user ID to promote to admin: "))
            promote_to_admin(user_id)
        elif choice == '3':
            user_id = int(input("Enter the user ID to delete: "))
            delete_user(user_id)
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    logging.info("Starting the Bookstore Application")
    main_menu()
    logging.info("Bookstore Application has ended")