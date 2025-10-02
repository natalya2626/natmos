num1 = int(input("Введите число 1: "))
num2 = int(input("Введите число 2: "))

if num1 > num2:
    print(f"Вывести: {num2}, {num1}")
elif num1 < num2:
    print(f"Вывести: {num1}, {num2}")
else:
    print("Числа равны")