
start = int(input())
end = int(input())

# 1. Все числа от start до end (по возрастанию)
current = start
while current <= end:
    print(current)
    current += 1

# 2. Все числа от end до start (по убыванию)
current = end # сброс!
while current >= start:
    print(current) 
    current -= 1

# 3. Числа, кратные 7
current = start  # сброс !
while current <= end:
    if current % 7 == 0:
        print(current)
    current += 1

# 4. Числа, кратные 5
count = 0
current =start  # сброс!
while current <= end:
    if current % 5 == 0:
        count += 1
    current += 1    
print(count)

    
