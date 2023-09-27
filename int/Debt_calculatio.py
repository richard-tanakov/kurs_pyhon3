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
