"""Программист решил купить квартиру стоимостью a рублей в ИТ-ипотеку на 3 года под y% годовых и с первоначальным взносом x рублей. Каждый год он выплачивает банку b рублей. Выведите остаток долга для банка на каждый год."""

full_amount = int(input())
percentages = int(input())
contribution = int(input())
payments = int(input())

debt = full_amount - contribution  # Долг с вычетов первого взноса.

debt = int((debt - payments) * (1 + percentages / 100))  # Рассчёт остатка на первый год
print(debt)

debt = int((debt - payments) * (1 + percentages / 100))  # Рассчёт остатка на второй год
print(debt)

debt = int((debt - payments) * (1 + percentages / 100))  # Рассчёт остатка на третий год
print(debt)
