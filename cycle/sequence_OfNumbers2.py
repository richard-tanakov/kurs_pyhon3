n = int(input())
k = -1
for i in range(n):

    k += 1
    if i % 2 == 0:
        for j in range(1, (n+1) - k):
            print(j, end=" ")

    else:
        for d in range(n, k, -1):
            print(d, end=' ')
    print()