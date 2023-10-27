chiper=str(input())
step=int(input())
out=''
for i in chiper:
    out+=chr((ord(i)-step- 97) % 26 + 97) #Две задачи шифратор и дешифратор, отличие в знаке на step
print(out)