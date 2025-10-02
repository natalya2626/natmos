
start = int(input())
end = int(input())

# Сохраняем оригинальные значения
current = start
while current <= end:
    print(current)
    current += 1

current = start  # сброс!
while current <= end:
    if current % 7 == 0:
        print(current)
    current += 1

#current =start  # сброс!

