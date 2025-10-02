try:

    day_week = int(input("Введите день недели (1-7): "))

    if day_week == 1:
        print("День недели: Понедельник")
    elif day_week == 2:
        print("День недели: Вторник")
    elif day_week == 3:
        print("День недели: Среда")
    elif day_week == 4:
        print("День недели: Четверг")
    elif day_week == 5:
        print("День недели: Пятница")
    elif day_week == 6:
        print("День недели: Суббота")
    elif day_week == 7:
        print("День недели: Воскресенье")
    else:
        print("Ошибка: число должно быть от 1 до 7!")

except ValueError:
    print("Ошибка: введите целое число!")
        
