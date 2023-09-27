starting, ending = int(input()), int(input())
num = 0
for i in range(starting, ending + 1):
    num += 1
    if (num % 2) == 0:
        print(i * (-1))
    else:
        print(i)
