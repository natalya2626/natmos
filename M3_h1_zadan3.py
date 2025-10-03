number1 = int(input())
number2 = int(input())


current = number1
while current <= number2:
    if current % 3 == 0  and current % 5 == 0:
        print("FizzBuzz")

    elif current % 3 == 0:
            print("Fizz")        

    elif current % 5 == 0:
            print("Buzz")
    else:
        print(current)
    current += 1




