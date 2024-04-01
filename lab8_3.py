class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.current_speed = 0
        self.max_speed = 200

    def get_info(self):
        return f"Car Model: {self.model}, Year: {self.year}, Color: {self.color}"

    def accelerate(self, increment):
        self.current_speed += increment
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def brake(self, decrement):
        self.current_speed -= decrement
        if self.current_speed < 0:
            self.current_speed = 0

    def get_speed(self):
        return f"Current Speed: {self.current_speed} km/h"

# Создаем объект класса Car
my_car = Car("Toyota Camry", 2022, "Red")

# Выводим информацию о машине
print(my_car.get_info())

# Ускоряемся до 150 км/ч
my_car.accelerate(150)
print(my_car.get_speed())

# Тормозим на 20 км/ч
my_car.brake(20)
print(my_car.get_speed())
class ElectricCar(Car):
    def __init__(self, model, year, color, battery_capacity):
        super().__init__(model, year, color)
        self.battery_capacity = battery_capacity

    def charge_battery(self):
        print("Charging the battery...")

# Создаем объект класса ElectricCar
my_electric_car = ElectricCar("Tesla Model S", 2023, "White", 100)

# Выводим информацию о машине
print(my_electric_car.get_info())

# Заряжаем батарею
my_electric_car.charge_battery()