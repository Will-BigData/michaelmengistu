import bcrypt
from db import get_db_connection



def sign_up(username, password, email, role='user'):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        try:
            cursor.execute(
                "INSERT INTO Users (username, password, email, role) VALUES (%s, %s, %s, %s)",
                (username, hashed_password, email, role)
            )
            connection.commit()
            print("User registered successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

def login(username, password):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            print("Login successful.")
            return user
        else:
            print("Invalid credentials.")
            return None