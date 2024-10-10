# food_entry.py

class FoodEntry:
    """Represents a single food entry."""

    def __init__(self, entry_id: int, date: str, food_name: str, quantity: float, calories: float):
        self.id = entry_id
        self.date = date
        self.food_name = food_name
        self.quantity = quantity
        self.calories = calories

    def to_dict(self) -> dict:
        """Converts the FoodEntry object to a dictionary."""
        return {
            'ID': self.id,
            'Date': self.date,
            'Food Name': self.food_name,
            'Quantity': self.quantity,
            'Calories': self.calories
        }
