class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
tesla = Vehicle(210, 30)
print(f"Tesla's top speed is {tesla.max_speed}")
print(f"Tesla's mileage is {tesla.mileage}")
mercedez = Vehicle(290, 23)
print(f"Mercedez's top speed is {mercedez.max_speed}")
print(f"Mercedez's mileage is {mercedez.mileage}")