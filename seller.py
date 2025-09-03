from typing import List
from car import Car

class Seller:
    def __init__(self, name: str, rating: float = 4.5):
        self.name = name
        self.rating = rating
        self.inventory: List[Car] = []

    def Buy(self, car: Car):
        if car in self.inventory:
            raise ValueError("Car already in inventory.")
        self.inventory.append(car)     # <-- must append

    def Sell(self, car: Car):
        if car not in self.inventory:
            raise ValueError("Car not in inventory.")
        self.inventory.remove(car)

    def list_brief(self, limit: int = 20):
        for idx, c in enumerate(self.inventory[:limit]):
            print(f"[{idx}] {c.year} {c.manufacturer} {c.model} | ${c.price:.0f} | {c.mileage:.0f} mi")
        if len(self.inventory) > limit:
            print(f"... and {len(self.inventory) - limit} more")
