# 3. Напишите функцию, которая принимает список строк и возвращает самую 
# длинную строку из него. Если список пуст, верните пустую строку.  


# def max_length_item(strings):  # Определяем функцию с именем max_length_item(махсимальная длина элемента), 
#                                # которая принимает один аргумент — strings. (строки)
#     max_string = strings[0]  # инициализируем переменную max_string первым элементом списка.
#                               # Это начальное предположение: «пока самая длинная строка — первая».
#     for item in strings:     # запускаем цикл по всем элементам списка strings.
#                              # На каждой итерации переменная item будет содержать очередную строку из списка. 

#         if len(item) > len(max_string): # Сравнивает длину текущей строки (item) с длиной самой 
#                                          # длинной строки, найденной на данный момент (max_string). 
#             max_string = item   # Если текущая строка длиннее, чем max_string, то обновляем рекорд:
#                                 # теперь max_string — это item. 
#     return max_string   # После завершения цикла функция возвращает строку максимальной длины.
words = 0
def max_length_item(strings):
    if not strings:
        return None  # или raise ValueError("Список пуст")
    max_string = strings[0]
    for item in strings:
        if len(item) > len(max_string):
            max_string = item
    return max_string
# words = ["кот", "слон", "бабочка", "ёж"]
# result = max_length_item(words)
# print(result)  # Выведет: "бабочка"