# cli.py

import sys
from typing import Optional
from food_manager import FoodManager
from food_entry import FoodEntry
from datetime import datetime
import re

class CLI:
    """Handles the command-line interface."""

    def __init__(self, manager: FoodManager):
        self.manager = manager

    def display_menu(self):
        """Displays the main menu."""
        print("\n=== Food Tracking App ===")
        print("1. View Food Entries")
        print("2. Add Food Entry")
        print("3. Update Food Entry")
        print("4. Delete Food Entry")
        print("5. Search Food Entries")
        print("6. Exit")

    def run(self):
        """Runs the CLI loop."""
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ").strip()
            if choice == '1':
                self.view_entries()
            elif choice == '2':
                self.add_entry()
            elif choice == '3':
                self.update_entry()
            elif choice == '4':
                self.delete_entry()
            elif choice == '5':
                self.search_entries()
            elif choice == '6':
                self.exit_program()
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

    def view_entries(self):
        """Displays all food entries."""
        if not self.manager.entries:
            print("\nNo food entries available.")
            return
        print("\n--- Food Entries ---")
        print(f"{'ID':<5} {'Date':<12} {'Food Name':<25} {'Quantity':<10} {'Calories':<10}")
        print("-" * 65)
        for entry in self.manager.entries:
            print(f"{entry.id:<5} {entry.date:<12} {entry.food_name:<25} {entry.quantity:<10} {entry.calories:<10}")

    def add_entry(self):
        """Adds a new food entry."""
        print("\n--- Add Food Entry ---")
        date = self.get_valid_input("Enter date (YYYY-MM-DD): ", self.validate_date)
        food_name = self.get_valid_input("Enter food name: ", self.validate_non_empty)
        quantity = self.get_valid_input("Enter quantity (e.g., number of servings): ", self.validate_positive_float)
        calories = self.get_valid_input("Enter calories per serving: ", self.validate_positive_float)
        self.manager.add_entry(date, food_name, float(quantity), float(calories))
        self.manager.save_entries()
        print("Food entry added successfully.")

    def update_entry(self):
        """Updates an existing food entry."""
        print("\n--- Update Food Entry ---")
        entry_id = self.get_valid_input("Enter food entry ID to update: ", self.validate_integer)
        entry = self.manager.find_entry_by_id(int(entry_id))
        if not entry:
            print(f"No food entry found with ID {entry_id}.")
            return
        print(f"Updating Food Entry ID {entry.id}: {entry.food_name} on {entry.date}")
        date = self.get_valid_input(f"Enter new date [{entry.date}]: ", self.validate_date, allow_empty=True)
        food_name = self.get_valid_input(f"Enter new food name [{entry.food_name}]: ", self.validate_non_empty, allow_empty=True)
        quantity = self.get_valid_input(f"Enter new quantity [{entry.quantity}]: ", self.validate_positive_float, allow_empty=True)
        calories = self.get_valid_input(f"Enter new calories [{entry.calories}]: ", self.validate_positive_float, allow_empty=True)

        if date:
            entry.date = date
        if food_name:
            entry.food_name = food_name
        if quantity:
            entry.quantity = float(quantity)
        if calories:
            entry.calories = float(calories)

        self.manager.save_entries()
        print("Food entry updated successfully.")

    def delete_entry(self):
        """Deletes a food entry."""
        print("\n--- Delete Food Entry ---")
        entry_id = self.get_valid_input("Enter food entry ID to delete: ", self.validate_integer)
        success = self.manager.delete_entry(int(entry_id))
        if success:
            self.manager.save_entries()
            print("Food entry deleted successfully.")
        else:
            print(f"No food entry found with ID {entry_id}.")

    def search_entries(self):
        """Searches for food entries."""
        print("\n--- Search Food Entries ---")
        keyword = input("Enter search keyword (food name or date): ").strip()
        if not keyword:
            print("Search keyword cannot be empty.")
            return
        results = self.manager.search_entries(keyword)
        if not results:
            print("No matching food entries found.")
            return
        print(f"\n--- Search Results ({len(results)} found) ---")
        print(f"{'ID':<5} {'Date':<12} {'Food Name':<25} {'Quantity':<10} {'Calories':<10}")
        print("-" * 65)
        for entry in results:
            print(f"{entry.id:<5} {entry.date:<12} {entry.food_name:<25} {entry.quantity:<10} {entry.calories:<10}")

    def exit_program(self):
        """Exits the program."""
        print("Exiting Food Tracking App. Goodbye!")
        sys.exit(0)

    def get_valid_input(self, prompt: str, validation_func, allow_empty: bool = False) -> Optional[str]:
        """Gets validated input from the user."""
        while True:
            user_input = input(prompt).strip()
            if allow_empty and user_input == '':
                return ''
            if validation_func(user_input):
                return user_input
            else:
                print("Invalid input. Please try again.")

    @staticmethod
    def validate_non_empty(input_str: str) -> bool:
        """Validates that the input is not empty."""
        return len(input_str) > 0

    @staticmethod
    def validate_date(date_str: str) -> bool:
        """Validates the date format (YYYY-MM-DD)."""
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_positive_float(value: str) -> bool:
        """Validates that the input is a positive float."""
        try:
            return float(value) > 0
        except ValueError:
            return False

    @staticmethod
    def validate_integer(value: str) -> bool:
        """Validates that the input is an integer."""
        return value.isdigit()
