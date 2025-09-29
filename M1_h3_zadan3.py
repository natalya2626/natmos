
# Ввод количества метров
meters = float(input("Введите количество метров: "))

# Константы перевода
CM_PER_METER = 100        # сантиметров в метре
DM_PER_METER = 10         # дециметров в метре
MM_PER_METER = 1000       # миллиметров в метре
METERS_PER_MILE = 1609.34 # метров в миле

# Перевод
centimeters = meters * CM_PER_METER
decimeters = meters * DM_PER_METER
millimeters = meters * MM_PER_METER
miles = meters / METERS_PER_MILE  # делим, потому что миль меньше, чем метров

# Вывод результатов
print(f"{meters} метров = {centimeters} сантиметров")
print(f"{meters} метров = {decimeters} дециметров")
print(f"{meters} метров = {millimeters} миллиметров")
print(f"{meters} метров = {miles:.6f} миль")