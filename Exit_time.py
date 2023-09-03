""" На вход вашему серверу пришло время в минутах, которое провел пользователь на сайте , а также время начала сессии. Вам нужно определить сколько времени было на цифровых часах у пользователя, когда он закрывал сайт.

Ваша программа получает на вход 3 переменные, каждая в новой строке:

time_mins – количество минут, которое пользователь провел на сайте
start_hours – время в часах, когда пользователь зашел на сайт
start_mins – время в минутах, когда пользователь зашел на сайт
Программа должна вывести через пробел количество часов и минут, когда пользователь закрыл сайт"""

time_mins = int(input())
start_hours = int(input())
start_mins = int(input())

time_mins = (start_hours * 60) + start_mins + time_mins
time_hours, time_mins = (time_mins // 60), (time_mins % 60)


if time_hours <= 24:
    print(time_hours, time_mins)
else:
    print((time_hours - 24), time_mins)
