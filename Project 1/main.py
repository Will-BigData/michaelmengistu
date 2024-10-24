from auth import sign_up, login, view_all_users, promote_to_admin, delete_user, user_exists
from crud import add_book, view_books, delete_book, create_order, update_book, view_order_history, book_exists
from utils import get_date_input, get_float_input, get_int_input
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
            print_books(books)
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
        print("4. Update a Book")
        print("5. View All Users")
        print("6. Promote User to Admin")
        print("7. Delete User")
        print("8. Log Out")
        choice = input("Select an option: ")

        if choice == '1':
            books = view_books()
            print_books(books)
        elif choice == '2':
            handle_add_book()
        elif choice == '3':
            handle_delete_book()
        elif choice == '4':
            handle_update_book()
        elif choice == '5':
            handle_view_all_users()
        elif choice == '6':
            handle_promote_user()
        elif choice == '7':
            handle_delete_user()
        elif choice == '8':
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")


def handle_add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    price = get_float_input("Enter price: ")
    stock_quantity = get_int_input("Enter stock quantity: ")
    publication_date = get_date_input("Enter publication date (YYYY-MM-DD): ")
    add_book(title, author, genre, price, stock_quantity, publication_date)

def handle_delete_book():
    book_id = get_int_input("Enter the book ID to delete: ")
    if book_id is not None:
        delete_book(book_id)
    else:
        print("Invalid book ID. Please enter a valid number.")

def handle_purchase():
    book_id = get_int_input("Enter the book ID to purchase: ")
    if book_id is None and book_exists(book_id):
        print("Invalid book ID. Please enter a valid number.")
        return

    quantity = get_int_input("Enter quantity: ")
    if quantity is None or quantity <= 0:
        print("Invalid quantity. Please enter a positive integer.")
        return

    create_order(current_user['user_id'], book_id, quantity)

def handle_view_orders():
    orders = view_order_history(current_user['user_id'])
    if orders:
        print("\nOrder History:")
        for order in orders:
            print(f"Order ID: {order['order_id']}, Book: {order['title']}, Quantity: {order['quantity']}, "
                  f"Total Price: ${order['total_price']}, Status: {order['status']}, Date: {order['order_date']}")
    else:
        print("No orders found.")

def handle_update_book():
    book_id = get_int_input("Enter the book ID to update: ")
    if(book_id is not None and book_exists(book_id)):

        title = input("Enter new title: ")
        author = input("Enter new author: ")
        genre = input("Enter new genre: ")
        price = get_float_input("Enter new price: ")
        stock_quantity = get_int_input("Enter new stock quantity: ")
        publication_date = get_date_input("Enter new publication date (YYYY-MM-DD): ")
        if stock_quantity is not None and stock_quantity < 0:
            print("Stock quantity cannot be negative. Setting it to 0.")
            stock_quantity = 0
    
        update_book(
            book_id,title,author,genre,price,stock_quantity,publication_date)
    else:
        print("Invalid book ID. Book does not exist.")


def handle_view_all_users():
    users = view_all_users()
    for user in users:
        print(f"{user['user_id']}: {user['username']} ({user['role']}) - {user['email']}")

def handle_promote_user():
    user_id = get_int_input("Enter the user ID to promote to admin: ")
    if user_id is not None and user_exists(user_id):
        promote_to_admin(user_id)
    else:
        print("Invalid user ID. User does not exist.")


def handle_delete_user():
    user_id = get_int_input("Enter the user ID to delete: ")
    if user_id is not None and user_exists(user_id):
        delete_user(user_id)
    else:
        print("Invalid user ID. User does not exist.")



def print_books( books ):
    for book in books:
        print(f"{book['book_id']}: {book['title']} by {book['author']} - ${book['price']} stock_quantity: {book['stock_quantity']}")







if __name__ == '__main__':
    logging.info("Starting the Bookstore Application")
    main_menu()
    logging.info("Bookstore Application has ended")