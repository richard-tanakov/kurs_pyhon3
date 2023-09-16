num = int(input())


print((num%2)==0) #Четное или не четное
print(num>0) # Положительное или отрицательное
print(-5<=num<=5) # Отрезок 
print((num%3 or num%4)==0 and num%7!=0)

if (num*(-1))>0: #Если число отричательное, умножаем на -1, чтобы получить положительное
    print((len(str(num*(-1))))==3)
else:
    print((len(str(num)))==3)
