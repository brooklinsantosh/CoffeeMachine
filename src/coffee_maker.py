from src.menu import MenuItem, Ingredients
from dataclasses import fields

class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self)-> None:
        self.resources = Ingredients(water= 300, milk= 200, coffee=100)

    def report(self)-> None:
        """Prints a report of all resources."""
        print(f"Water: {self.resources.water}ml")
        print(f"Milk: {self.resources.milk}ml")
        print(f"Coffee: {self.resources.coffee}g")

    def is_resource_sufficient(self, item: MenuItem)-> bool:
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for field in fields(item.ingredients):
            if getattr(item.ingredients, field.name) > getattr(self.resources, field.name):
                print(f"Sorry there is not enough {field.name}.")
                can_make = False
        return can_make

    def make_coffee(self, item: MenuItem)-> None:
        """Deducts the required ingredients from the resources."""
        self.resources.water -= item.ingredients.water
        self.resources.milk -= item.ingredients.milk
        self.resources.coffee -= item.ingredients.coffee
        print(f"Here is your {item.name} ☕️. Enjoy!")
