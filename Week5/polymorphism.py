# Parent class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Car subclass
class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"

# Plane subclass
class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"

# Boat subclass
class Boat(Vehicle):
    def move(self):
        return "⛵ Sailing on water"

# Example
vehicles = [Car(), Plane(), Boat()]   # List of different vehicle objects

for v in vehicles:
    print(v.move())   # Each object responds in its own way (polymorphism)
