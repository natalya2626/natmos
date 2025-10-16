# Пользователь вводит с клавиатуры числа. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Numberis negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит ,

# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит 
# число 7 программа прекращает свою работу и выводит 
# на экран надпись "Good bye"

while True:
    
    number =int(input())
    if number == 7:
       break
    if number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
    else:
        print("zero")    
print("Good bye")        

       
