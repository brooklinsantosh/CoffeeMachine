from dataclasses import dataclass

@dataclass
class Ingredients:
    """Data class to store ingredients"""
    water: int
    milk: int
    coffee: int

@dataclass
class MenuItem:
    """Data class to store the details of items in the menu"""
    name: str
    cost: float
    ingredients: Ingredients

class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", cost=2.5, ingredients=Ingredients(milk=150, coffee=24, water=200)),
            MenuItem(name="espresso", cost=1.5, ingredients=Ingredients(milk=0, coffee=18, water=50)),
            MenuItem(name="cappuccino", cost=3, ingredients=Ingredients(milk=50, coffee=24, water=250)),
        ]
    
    def get_items(self)-> str:
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_item(self, order_name: str)-> MenuItem:
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

