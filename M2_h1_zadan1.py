# Ввод трех чисел
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

# Выбор пользователя 
print("Выберите операцию: ")
print("1 -- Суммa")
print("2 -- произведение")

choice = input("Ваш выбор (1 или 2): ")

# Вычисление и вывод результата
if choice == "1":
    result = a + b + c 
    print("Сумма чисел: ",result)
elif choice == "2":
    result = a * b* c
    print("Произведение чисел: ", result)
else:
    print("Ошибка: нужно ввести 1 или 2.")