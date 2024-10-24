from db import get_db_connection
from db import logging


#Add a book:
def add_book(title, author, genre, price, stock_quantity, publication_date):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO Books (title, author, genre, price, stock_quantity, publication_date) VALUES (%s, %s, %s, %s, %s, %s)",
                (title, author, genre, price, stock_quantity, publication_date)
            )
            connection.commit()
            logging.info(f"Book '{title}' added to inventory.")
        except Exception as e:
            logging.error(f"Failed to add book: {e}")
        finally:
            cursor.close()
            connection.close()


#Update a book:
def update_book(book_id, **kwargs):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            updates = ", ".join(f"{k} = %s" for k in kwargs.keys())
            sql = f"UPDATE Books SET {updates} WHERE book_id = %s"
            cursor.execute(sql, list(kwargs.values()) + [book_id])
            connection.commit()
            print("Book updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()


#Create a order:
def create_order(user_id, book_id, quantity):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT price, stock_quantity FROM Books WHERE book_id = %s", (book_id,))
            book = cursor.fetchone()
            if book and book[1] >= quantity:
                total_price = book[0] * quantity
                cursor.execute(
                    "INSERT INTO Orders (user_id, book_id, quantity, total_price, status) VALUES (%s, %s, %s, %s, 'completed')",
                    (user_id, book_id, quantity, total_price)
                )
                cursor.execute("UPDATE Books SET stock_quantity = stock_quantity - %s WHERE book_id = %s", (quantity, book_id))
                connection.commit()
                logging.info(f"Order placed by user_id {user_id} for book_id {book_id} (quantity: {quantity}).")
            else:
                print(f"Sorry, we only have {book[1]} in stock. Please try to reorder again.")
                logging.warning(f"Failed order attempt due to insufficient stock for book_id {book_id}.")
        except Exception as e:
            print(f"Sorry, book ID = {book_id} does not exist. Please try again.")
            logging.error(f"Error creating order: {e}")
        finally:
            cursor.close()
            connection.close()



#View Books:
def view_books():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM Books")
            books = cursor.fetchall()
            return books
        except Exception as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()
            connection.close()

#Delete a Book:
def delete_book(book_id):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM Books WHERE book_id = %s", (book_id,))
            connection.commit()
            print("Book deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()



#view order history
def view_order_history(user_id):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("""
                SELECT o.order_id, b.title, o.quantity, o.total_price, o.status, o.order_date
                FROM Orders o
                JOIN Books b ON o.book_id = b.book_id
                WHERE o.user_id = %s
                ORDER BY o.order_date DESC
            """, (user_id,))
            orders = cursor.fetchall()
            return orders
        except Exception as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()
            connection.close()