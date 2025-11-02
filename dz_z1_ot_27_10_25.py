# Задание 1. Создайте  функцию, которая принимает целое число в качестве 
# аргумента и возвращает "Еven" для четных чисел или "Odd" для нечетных  чисел.

def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even(4))
print(check_even(7))
print(check_even(28))
print(check_even(100))
print(check_even(0))

# Задание 2. Дополните метод, который принимает логическое значение и возвращает строку «Да»
# для значения «истина» или строку «Нет» для значения «ложь».  

def bool_to_string(value: bool) -> str:
    if value:
        return "Да"
    else:
        return "Нет"  
print(bool_to_string("я на прогулке")) 
print(bool_to_string(True))

# Задание3. Ваша цель — написать функцию, которая удаляет первый и последний символы строки.
# Вам дан один параметр — исходная строка.

def remove_edges(text):
    return text[1:-1]
print(remove_edges("wallet"))
