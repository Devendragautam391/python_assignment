class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.kilometers_driven = 0

    def drive(self, hours, speed):
        actual_speed = min(speed, self.max_speed)
        self.kilometers_driven += actual_speed * hours

    def __str__(self):
        return (f"Registration: {self.registration_number}\n"
                f"Max Speed: {self.max_speed} km/h\n"
                f"Kilometers Driven: {self.kilometers_driven} km")

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nBattery Capacity: {self.battery_capacity} kWh"

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nTank Volume: {self.tank_volume} l"

if __name__ == "__main__":
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    electric_car.drive(3, 180)
    gasoline_car.drive(3, 160)

    print("Electric Car Info:")
    print(electric_car)
    print("\nGasoline Car Info:")
    print(gasoline_car)
