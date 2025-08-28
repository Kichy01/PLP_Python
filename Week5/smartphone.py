# Parent class: Smartphone
class Smartphone:
    # Constructor (__init__) initializes attributes when a new object is created
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery
    
    # Method to simulate making a call
    def call(self, number):
        return f"📞 Calling {number} from {self.model}..."
    
    # Method to charge the phone battery
    def charge(self, amount):
        self.battery += amount
        if self.battery > 100:   # Battery cannot exceed 100%
            self.battery = 100
        return f"🔋 {self.model} charged to {self.battery}%"

# Child class: GamingPhone (inherits from Smartphone)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        # super() allows us to reuse Smartphone's constructor
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    # Polymorphism: overriding the call() method from the parent class
    def call(self, number):
        return f"📞 Calling {number} with Gaming Mode ON 🎮 using {self.model}!"

    # Extra method unique to GamingPhone
    def play_game(self, game):
        if self.battery > 20:
            self.battery -= 20   # Gaming consumes more battery
            return f"🎮 Playing {game} on {self.model}... Battery now {self.battery}%"
        else:
            return f"⚠️ Battery too low to play {game}!"

# Usage examples
phone1 = Smartphone("Samsung", "Galaxy S23", "256GB", 75)
gaming_phone = GamingPhone("Asus", "ROG Phone 7", "512GB", 90, "Advanced Cooling")

print(phone1.call("+254730456789"))
print(phone1.charge(10))
print(gaming_phone.call("+233730456789"))
print(gaming_phone.play_game("Call of Duty Advanced Warfare"))
print(gaming_phone.charge(15))

