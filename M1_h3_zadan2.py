
n = int(input("Введите четырехзначное число: "))

# Требуется найти произведение цифр

first_digit = int(str(n)[0])
second_digit = int(str(n)[1])
fhird_digit = int(str(n)[2])
four_digit = int(str(n)[3])

product_numbers = first_digit*second_digit*fhird_digit*four_digit
print(product_numbers)