# Ввод метров 
m = float(input("Введите количество метров: "))
           
# Выбор пользователя 
print( "Выберите операцию: ")
print("1 - Перевести метры в мили (сухопутные)")
print("2 - Перевести метры в дюймы")
print("3 -Перевести метры в ярды")

choice = input("Ваш выбор (1, 2 или 3): ")

#Константы: сколько метров в одной единице
METERS_IN_MILE  = 1609.344  # стандартное значение
METERS_IN_INCH  = 0.0254    # точно по определению
METERS_IN_YARD  = 0.9144    # стандартное значение

# Вычисление и вывод результата
if choice == "1":
    result = m/METERS_IN_MILE
    print(f"Получислось миль: {result:.6f}")
elif choice == "2":
    result = m/METERS_IN_INCH
    print(f"Получилось дюймов: {result:.2f}")
elif choice  == "3":
    result = m/METERS_IN_YARD
    print(f"Получилось ярдов: {result:.2f}")

else:
    print("Ошибка: нужно ввести 1, 2 или 3.")