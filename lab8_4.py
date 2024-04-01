class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.__max_speed = 200  # Приватный атрибут максимальной скорости

    def get_info(self):
        return f"Car Model: {self.model}, Year: {self.year}, Color: {self.color}"

    def accelerate(self, increment):
        self.current_speed += increment
        if self.current_speed > self.__max_speed:
            self.current_speed = self.__max_speed

    def brake(self, decrement):
        self.current_speed -= decrement
        if self.current_speed < 0:
            self.current_speed = 0

    def get_speed(self):
        return f"Current Speed: {self.current_speed} km/h"

    # Методы для доступа к приватному атрибуту max_speed
    def get_max_speed(self):
        return self.__max_speed

    def set_max_speed(self, new_max_speed):
        self.__max_speed = new_max_speed

# Создаем объект класса Car
my_car = Car("Toyota Camry", 2022, "Red")

# Выводим информацию о машине
print(my_car.get_info())

# Получаем текущую максимальную скорость
print("Max Speed:", my_car.get_max_speed())

# Устанавливаем новую максимальную скорость
my_car.set_max_speed(250)

# Выводим обновленную информацию о машине
print("Max Speed:", my_car.get_max_speed())
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