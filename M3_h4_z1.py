# Задание 1
# Показать на экран все простые числа в диапазоне,
# указанном пользователем. Число называется простым,
# если оно делится без остатка только на себя и на единицу.
# Например, три — это простое число, а четыре нет.

start = int(input())
end = int(input())


for n in range(start, end+1):
    if n < 2:
        continue

    is_prime = True
    for divisor in range(2, n):     
       if n % divisor == 0:
           is_prime = False
           break
       
    if is_prime:  
        print(n)
        
