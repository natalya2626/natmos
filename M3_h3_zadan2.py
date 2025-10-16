# Подсчитать количество целых чисел в диапазоне от
# 100 до 999 у которых есть две одинаковые цифры.

#number =int(input())

# count = 0 
 

# for number in range(100,1000):
#     digit3 = number % 10
#     number //= 10
#     digit2 = number % 10
#     number //= 10
#     digit1 = number % 10
    
#     if (digit1 == digit2 and digit1 != digit3 or
#     digit1 == digit3 and digit1 != digit2 or
#     digit2 == digit3 and digit2 != digit1):
    
#     count += 1
# print(count)

count = 0

for n in range(100, 1000):
    d1 = n // 100          # сотни
    d2 = (n // 10) % 10    # десятки
    d3 = n % 10            # единицы
    
    if (d1 == d2 and d1 != d3 or
        d1 == d3 and d1 != d2 or
        d2 == d3 and d2 != d1):
        count += 1

print(count)