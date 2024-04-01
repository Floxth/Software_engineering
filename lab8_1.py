class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def get_info(self):
        return f"Car Model: {self.model}, Year: {self.year}, Color: {self.color}"

# Создаем объект класса Car
my_car = Car("Toyota Camry", 2022, "Red")

# Выводим информацию о машине
print(my_car.get_info())
