try:

    count = int(input("Начало диапазона: "))
    end = int(input("Конец диапазона: "))


    while count <= end:
        if count % 7 == 0:
            print(count)
        count += 1  
     
except ValueError:
    print("Пожалуйста, введите целые числа!")