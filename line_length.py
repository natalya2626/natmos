line_length = int(input())
symbol = input()

while line_length > 0:
    print(f"{symbol:^100}")
    line_length -= 1