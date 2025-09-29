
# Ввод трех чисел
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

# Выбор пользователя
print("Выберите операцию: ")
print("1 -- максимум из трех")
print("2 -- минимум из трех")
print("3 -- среднеарифметическое трех чисел")

choice = input ("Ваш выбор (1, 2 или 3):  ")

# Обработка выбора
if choice  == "1":
    result = max(num1, num2, num3)
    print("Максимум из  трех чисел: ", result)

elif choice == "2":
      result = min(num1, num2,num3)
      print("Минимум из трех чисел: ", result)

elif choice == "3":
     result = (num1 + num2 +num3)/3
     print("Среднеарифметическое из трех чисел: ", result) 
else:
     print("Oшибка: нужно ввести 1, 2 или 3.")


