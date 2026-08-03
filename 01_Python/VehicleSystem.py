class vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")
    def start_engine(self):
        print("Engine started.")

class Car(vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
        
    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")
        
    def start_engine(self):
        print("Car engine started.")
        
class Motorcycle(vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar
        
    def display_info(self):
        super().display_info()
        print(f"Has sidecar: {self.has_sidecar}")
        
    def start_engine(self):
        print("Motorcycle engine started.")

class Truck(vehicle):
    def __init__(self, brand, model, year, payload_capacity):
        super().__init__(brand, model, year)
        self.payload_capacity = payload_capacity
        
    def display_info(self):
        super().display_info()
        print(f"Payload capacity: {self.payload_capacity} kg")
        
    def start_engine(self):
        print("Truck engine started.")
        
Car1 = Car("Toyota", "Camry", 2020, 4)
Car1.display_info()
Car1.start_engine()
motorcycle1 = Motorcycle("Harley-Davidson", "Street 750", 2019, False)
motorcycle1.display_info()
motorcycle1.start_engine()
truck1 = Truck("Ford", "F-150", 2021, 1000)
truck1.display_info()
truck1.start_engine()