import mysql.connector
import logging

# Configure logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='project1-database.c7mw0q00637k.us-east-2.rds.amazonaws.com',
            user='admin',
            password='NBJbQex2YKAlcern4go4',
            database='bookstore'
        )
        logging.info("Connected to the database successfully.")
        return connection
    except mysql.connector.Error as err:
        logging.error(f"Error: {err}")
        return None