#extra functions for error handling
from datetime import datetime

def get_date_input(prompt):
    while True:
        user_input = input(prompt).strip()  # Remove leading/trailing whitespace
        if user_input == "":
            return None  # Allow blank input
        try:
            # Specify the date format you expect (e.g., 'YYYY-MM-DD')
            date = datetime.strptime(user_input, '%Y-%m-%d')
            return date
        except ValueError:
            print("Invalid input. Please enter a valid date in the format YYYY-MM-DD or leave it blank.")

def get_float_input(prompt):
    while True:
        user_input = input(prompt).strip()  # Remove leading/trailing whitespace
        if user_input == "":
            return None  # Allow blank input
        try:
            # Try to convert the input to a float
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid float or leave it blank.")

def get_int_input(prompt):
    while True:
        user_input = input(prompt).strip()  # Remove leading/trailing whitespace
        if user_input == "":
            return None  # Allow blank input
        try:
            # Try to convert the input to an integer
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer or leave it blank.")