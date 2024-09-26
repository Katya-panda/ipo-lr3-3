day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
if month in [3, 4, 5]:
        season = "Весна"
elif month in [6, 7, 8]:
        season = "Лето"
elif month in [9, 10, 11]:
        season = "Осень"
elif month in [12, 1, 2]:
        season = "Зима"
else:
        season = "Некорректный месяц"
print(f"Сезон: {season}")