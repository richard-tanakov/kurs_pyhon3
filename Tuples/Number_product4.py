nums=[int(i) for i in input().split()]
score=nums.count(0)
delN=0
nums=list(filter((delN).__ne__,nums))
if score==0: 
    print(*nums)

else:
    out=nums+([0]*score)
    print(*out)