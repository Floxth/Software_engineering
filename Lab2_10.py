user_info = input("Введите имя, фамилию и город в котором живёшь через пробел: ")
name, surname, city = user_info.split()
greeting = f"Привет, {name} {surname}! Ты живёшь в городе {city}."
print(greeting)