class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def get_info(self):
        return f"Car Model: {self.model}, Year: {self.year}, Color: {self.color}"


class SportsCar(Car):
    def __init__(self, model, year, color, top_speed):
        super().__init__(model, year, color)
        self.top_speed = top_speed

    def get_info(self):
        return f"Sports Car Model: {self.model}, Year: {self.year}, Color: {self.color}, Top Speed: {self.top_speed} km/h"


class SUV(Car):
    def __init__(self, model, year, color, seating_capacity):
        super().__init__(model, year, color)
        self.seating_capacity = seating_capacity

    def get_info(self):
        return f"SUV Model: {self.model}, Year: {self.year}, Color: {self.color}, Seating Capacity: {self.seating_capacity}"


# Создаем объекты различных типов автомобилей
my_sports_car = SportsCar("Ferrari 488 GTB", 2023, "Red", 330)
my_suv = SUV("Toyota Highlander", 2022, "Silver", 7)

# Выводим информацию о каждом автомобиле
print(my_sports_car.get_info())
print(my_suv.get_info())
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