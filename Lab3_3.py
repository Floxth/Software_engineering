number = input("Введите число от 0 до 10: ")
try:
    number = int(number)
    if 0 <= number <= 10:
        if number <= 3: print("Число находится в диапазоне от 0 до 3 включительно.")
        elif number <= 6: print("Число находится в диапазоне от 3 до 6.")
        else: print("Число находится в диапазоне от 6 до 10 включительно.")
    else: print("Число не входит в диапазон от 0 до 10.")
except ValueError:
    print("Ошибка: введено не числовое значение.")