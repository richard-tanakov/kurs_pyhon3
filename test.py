yy = float(input())
xy = float(input())

cent1 = yy * 100
cent2 = xy * 100
m = int(cent1 + cent2)

vacation = (10 * m // 100)

food = (30 * m // 100)
payment = (5 * m // 100)
recreation = (15 * m // 100)
capital = m - (vacation + food + payment + recreation)
print('Отпуск:' ,(vacation // 100), 'руб.', (vacation % 100), 'коп.')
print('Пропитание и еда:'  ,(food // 100), 'руб.' ,(food % 100), 'коп.')
print('Коммунальные платежи:' , (payment // 100), 'руб.', (payment % 100), 'коп.')
print('Досуг:' , (recreation // 100), 'руб.', (recreation % 100), 'коп.')
print('Накопления:' , (capital // 100), 'руб.', (capital % 100), 'коп.')
