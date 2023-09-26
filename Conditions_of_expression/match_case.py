match dialogue:= str(input()):
    case 'Привет':
        print('Привет!')
    case 'Как дела?': 
        print('Все классно!')    
    case 'Пока':
        print('До скорой встречи!')
    case _:
        print('Прости, я еще не знаю таких фраз :(')