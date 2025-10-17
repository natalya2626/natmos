# Модуль3 Циклы. Часть 4. задание 4
# Пользователь вводит с клавиатуры длину и ширину
# прямоугольника. Требуется отобразить на экран 
# незаполненный прямоугольник (отображаются только
#  границы прямоугольника). Размер длины и ширины равен
#  веденным данным

rows_count = int(input())
cols_count = int(input())

for row in range(rows_count):
    # print ('работает первый (внешний) цикл') 
    for col in range(cols_count):
        # print('работает второй (внутренний цикл')
        if (
            row == 0 or row == rows_count - 1 or
            col == 0 or col == cols_count -1 

        ):
            print('*', end=' ')
        else:
            print(' ', end=' ')    
    print()        