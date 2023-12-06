nums=[int(i) for i in input().split()]
out=[]
for i in nums:
    if i % 2==0:
        out.append(i)
print(*out)