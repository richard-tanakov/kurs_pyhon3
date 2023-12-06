nums, score,out = [int(i) for i in input().split()], 1,''
for i in nums[0:len(nums)-1]:
    out+=str(i+int(nums[score]))+" "
    score+=1
print(out, end='')
    
