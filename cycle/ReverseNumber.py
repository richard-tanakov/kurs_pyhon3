num=str(input())
num1=num[::-1]
score=0
for i in (num1):
    if int(i)==0:
        score+=1
    else:
        break
if int(num)==0:
    print(num) 
else:
    print(num1[score:])