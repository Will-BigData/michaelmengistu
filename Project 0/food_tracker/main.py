# main.py

from food_manager import FoodManager
from cli import CLI

def main():
    manager = FoodManager('food_entries.csv')
    cli = CLI(manager)
    cli.run()

if __name__ == "__main__":
    main()
