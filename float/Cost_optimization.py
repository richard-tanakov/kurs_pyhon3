"""10 % доходов идут на отпуск
30 % доходов на пропитание и еду
5 % на коммунальные платежи
15 % на выходной досуг
остальные 40% идут в накопления"""

income_girl = float(input()) * 100
income_man = float(input()) * 100  # На вход подаётся доход двух людей.
income = int(income_girl + income_man)


def whole_sum_calculation(
    income,
):  # Для того чтобы вывести копейки нужно результаты функции %100, а целую часть на //100. Сделаем на выводе.
    vacation = 10 * income // 100  # Отпуск
    needs = 30 * income // 100  # Нужды
    communal = 5 * income // 100  # Коммуналка
    leisure = 15 * income // 100  # Досуг
    saving = income - (vacation + needs + communal + leisure)
    withdrawal(income, vacation, needs, communal, leisure, saving)


def withdrawal(income, vacation, needs, communal, leisure, saving):
    print("Отпуск:", (vacation // 100), "руб.", (vacation % 100), "коп.")
    print("Пропитание и еда:", (needs // 100), "руб.", (needs % 100), "коп.")
    print("Коммунальные платежи:", (communal // 100), "руб.", (communal % 100), "коп.")
    print("Досуг:", (leisure // 100), "руб.", (leisure % 100), "коп.")
    print("Накопления:", (saving // 100), "руб.", (saving % 100), "коп.")


whole_sum_calculation(income)  # запуск расчётов
