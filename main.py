class Tomato:
    states = {'отсутствует': 0, 'цветение': 1, 'зеленый': 2, 'красный': 3}

    def __init__(self, index):
        self._index = index  # Динамическое свойство, индекс помидора
        self._state = 'отсутствует'  # Динамическое свойство, стадия созревания

    def grow(self):
        if self._state != 'красный':
            current_index = self.states[self._state]
            self._state = list(self.states.keys())[current_index + 1]

    def is_ripe(self):
        return self._state == 'красный'


class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name  # Динамическое свойство, имя садовника
        self._plant = plant  # Динамическое свойство, объект класса TomatoBush

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Урожай собран!")
            self._plant.give_away_all()
        else:
            print("Помидоры еще не дозрели, подождите немного.")

    @staticmethod
    def knowledge_base():
        print("""
        Справка по садоводству:
        1. Ухаживайте за растениями, следите за их состоянием и переводите на следующие стадии созревания.
        2. Помидоры собираются, когда они становятся красными.
        """)


# Тесты
# 1. Вызов справки по садоводству
Gardener.knowledge_base()

# 2. Создание объектов классов TomatoBush и Gardener
bush = TomatoBush(5)
gardener = Gardener("Иван", bush)

# 3. Уход за кустом с помидорами
print("\nУход за кустом:")
print("Состояние томатов до ухода:", [tomato._state for tomato in bush.tomatoes])
gardener.work()
print("Состояние томатов после ухода:", [tomato._state for tomato in bush.tomatoes])

# 4. Попытка собрать урожай, когда томаты еще не созрели
print("\nПопытка собрать урожай до созревания всех помидоров:")
gardener.harvest()

# 5. Сбор урожая
print("\nСбор урожая после созревания всех помидоров:")
while not bush.all_are_ripe():
    gardener.work()
gardener.harvest()