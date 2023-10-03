num = int(input())
k = -1
for i in range(num):
    k += 1
    for j in range(num, k, -1):
        print(j, end=" ")

    print()
