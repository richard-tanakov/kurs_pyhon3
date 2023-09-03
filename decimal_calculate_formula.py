import decimal

num1,num2 = str(input()),str(input()) #Ввод чисел
out=decimal.getcontext().prec=60 #Задаем знаки после запятой
out=(decimal.Decimal(num1).sqrt()+decimal.Decimal(num2))
print(out)
