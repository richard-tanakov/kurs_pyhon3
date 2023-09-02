import decimal 


income= (30000.50+20000.75) # По условиям задачи подаётся два дохода. 

vacation=(income*10/100) #Отпуск
needs=(income*30/100)    #Нужды
apartment=(income*5/100)   #Комуналка
leisure=(income*15/100) #Досуг
savings=(income*40/100)  #Накопления


def penny (vacation,needs,apartment,leisure,savings): # Вычисление копеек
    vacation_penny= str(vacation-int(vacation))[+2:5] # [+2:4] Выводить две цифры после точки
    needs_penny=str(needs-int(needs))[+2:4]
    apartment_penny=str(apartment-int(apartment))[+2:4]
    leisure_penny=str(leisure-int(leisure))[+2:4]
    
    conclusion(vacation,)

penny (vacation,needs,apartment,leisure,savings)


