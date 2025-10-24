# 1. Напишите функцию, которая принимает список чисел и возвращает сумму всех элементов списка.

def sum_numbers(numbers):
   return sum(numbers)
print(sum_numbers([1, 25, 30, 40]))

# 2. Напишите функцию, которая принимает список и возвращает новый список,
#  содержащий только чётные числа из исходного. 

def even_numbers(numbers): 
    even_numbers_new = []
    for item in numbers:
        if item % 2 == 0:
            even_numbers_new.append(item)
    return even_numbers_new
print(even_numbers([1, 20, 35, 80, 101, 120]))   

# 4. Напишите функцию, которая принимает список и число, и возвращает True,
#  если это число встречается в списке ровно один раз.  

def list_numbers(numbers, number):
    count = 0 
    for item in numbers:
        if item == number:
            count += 1
    return count == 1  
print(list_numbers([1, 2, 3, 4], 3)) 

#тоже самое с помощью метода count()  

def list_numbers1(numbers, number):
    return numbers.count(number) == 1
print(list_numbers([10], 10)) 


# 5. Напишите функцию, которая принимает список чисел и возвращает
#  список из их квадратов (например, [1, 2, 3] → [1, 4, 9]).  

def sguare_list(numbers): 
    result = []
    for num in numbers:
       result.append(num**2)
    return result   
print(sguare_list([1, 2, 3, 4, 5]))    

