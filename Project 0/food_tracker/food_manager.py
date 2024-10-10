# food_manager.py

import csv
import os
from typing import List
from food_entry import FoodEntry

class FoodManager:
    """Manages the list of food entries."""

    def __init__(self, filename: str):
        self.filename = filename
        self.entries: List[FoodEntry] = []
        self.load_entries()

    def load_entries(self):
        """Loads food entries from the CSV file."""
        if not os.path.exists(self.filename):
            # Create the file with headers if it doesn't exist
            with open(self.filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['ID', 'Date', 'Food Name', 'Quantity', 'Calories'])
                writer.writeheader()
            return

        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    entry = FoodEntry(
                        entry_id=int(row['ID']),
                        date=row['Date'],
                        food_name=row['Food Name'],
                        quantity=float(row['Quantity']),
                        calories=float(row['Calories'])
                    )
                    self.entries.append(entry)
                except (ValueError, KeyError):
                    # Skip rows with invalid data
                    continue

    def save_entries(self):
        """Saves food entries to the CSV file."""
        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['ID', 'Date', 'Food Name', 'Quantity', 'Calories'])
            writer.writeheader()
            for entry in self.entries:
                writer.writerow(entry.to_dict())

    def get_next_id(self) -> int:
        """Returns the next available ID."""
        if not self.entries:
            return 1
        return max(entry.id for entry in self.entries) + 1

    def add_entry(self, date: str, food_name: str, quantity: float, calories: float):
        """Adds a new food entry."""
        new_entry = FoodEntry(
            entry_id=self.get_next_id(),
            date=date,
            food_name=food_name,
            quantity=quantity,
            calories=calories
        )
        self.entries.append(new_entry)

    def find_entry_by_id(self, entry_id: int) -> FoodEntry:
        """Finds a food entry by ID."""
        for entry in self.entries:
            if entry.id == entry_id:
                return entry
        return None

    def delete_entry(self, entry_id: int) -> bool:
        """Deletes a food entry by ID. Returns True if deleted, False otherwise."""
        entry = self.find_entry_by_id(entry_id)
        if entry:
            self.entries.remove(entry)
            return True
        return False

    def search_entries(self, keyword: str) -> List[FoodEntry]:
        """Searches food entries by food name or date."""
        keyword_lower = keyword.lower()
        return [
            entry for entry in self.entries
            if keyword_lower in entry.food_name.lower() or keyword_lower in entry.date
        ]
