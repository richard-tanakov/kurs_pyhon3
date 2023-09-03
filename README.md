# **Задачи на программирование с курса на Stepik. "Python-Разработчик".** [Ссылка на сам курс.](https://stepik.org/course/122813/syllabus)

## В данном репозитории находятся мои варианты решений с данного курса. В данном файле условия к задачам и ссылки на их решения. 

### Содержание:
+ [Арифметические действия.](#Арифметические-действия)
    + [Целые числа.](#Целые-числа)
        
   
   
   
   
   
### *Арифметические действия* 
   
 #### Целые числа
     

1. **Задача.** 

   > Напишите программу, которая получает на вход переменные a,b,c и рассчитывает формулу ( a в тепени c + b в стрепени
    c) скомбки в степени ab
    Программа должна вывести результат вычислений.

    2) Задача на программирование.

    Представим, что вы разработчик серверных приложений. У вас есть потребность в измерении количества времени, которое
    проводят ваши пользователи на сайте. Фронтенд посылает вам время в минутах, которое пользователь провел на сайте.
    Вам в ответ нужно узнать сколько в этих минутах часов и минут.

    Или иными словами:

    Ваша программа принимает одну переменную m – количество минут, которое пользователь провел на сайте. Вам нужно
    определить сколько в этих минутах часов и оставшихся минут. 

    ##### [Решение](https://github.com/richard-tanakov/richard-tanakov-stepik_developer_python/blob/main/Time_on_the_site.py)

    3) Задача:

    На вход вашему серверу пришло время в минутах, которое провел пользователь на сайте , а также время начала сессии.
    Вам нужно определить сколько времени было на цифровых часах у пользователя, когда он закрывал сайт.

    Ваша программа получает на вход 3 переменные, каждая в новой строке:

    time_mins – количество минут, которое пользователь провел на сайте
    start_hours – время в часах, когда пользователь зашел на сайт
    start_mins – время в минутах, когда пользователь зашел на сайт
    Программа должна вывести через пробел количество часов и минут, когда пользователь закрыл сайт

    Решение. Exit_time.py

    4)

    Задача:

    Пользователь сидит на сайте в среднем a минут и b секунд в день. Определите, сколько времени он будет находиться на
    сайте в течение n дней.

    Ваша программа получает на вход 3 переменные, каждая в новой строке:

    a – количество минут

    b – количество секунд

    n – количество дней

    В качестве результата программа должна вывести через пробел количество часов, минут и секунд, которые человек провел
    на сайте.

    Решение: Average_time_site.py

    Задача:

    Программист решил купить квартиру стоимостью a рублей в ИТ-ипотеку на 3 года под y% годовых и с первоначальным
    взносом x рублей. Каждый год он выплачивает банку b рублей. Выведите остаток долга для банка на каждый год.

    Например, если квартира стоит 10 000 000 , ставка 5 % годовых, первоначальный взнос 1 000 000, а платит программист
    3 000 000, тогда

    Кредит: 10 000 000 - 1 000 000 = 9 000 000

    Первый год:
    Остаток: (9 000 000 - 3 000 000) * (1 + 5 / 100) = 6 300 000

    Второй год:
    Остаток: (6 300 000 - 3 000 000) * (1 + 5 /100) = 3 465 000

    Третий год:
    Остаток: (3 465 000 - 3 000 000) * (1 + 5 /100) = 488 250

    Вашей программе на вход идут переменные:

    a – стоимость квартиры,
    y – процент годовых,
    x – первоначальный взнос,
    b – ежегодная выплата.
    Стоимость квартиры всегда больше суммы взносов. На каждом этапе расчетов отбрасывайте остатки с помощью int.

    Вам нужно вывести долг банку на каждый год трехлетнего кредита. Каждое число нужно вывести в новой строке.

    Решение: Debt_calculatio.py



    Числа с плавующей точкой.

    Задача. Задача на программирование
    Напишите программу, которая считывает переменные a, b, c и вычисляет формулу:
    �
    ( Позже рассписать уравнение)

    На вход вашей программе идут 3 числа a, b, c типа float.

    В качестве результата выведите ответ для формулы.

    Решение: Equation_floating_number.py




    Задача:

    Дано дробное число x. Выведите вторую цифру после точки.

    Решение: The_second_number.py

    Задача:

    Семья решила заняться оптимизацией своих денежных расходов и придумала следующую схему:

    10 % доходов идут на отпуск
    30 % доходов на пропитание и еду
    5 % на коммунальные платежи
    15 % на выходной досуг
    остальные 40% идут в накопления
    Если вдруг нужный процент не получается сделать, тогда копейка перекидывается в накопления. Например:

    Сумма доходов равна 50 001.25 , 10 % от этой суммы это 5000.125 рублей. Пол копейки как валюты не существует,
    поэтому эта половинка переходит в накопления.

    Напишите для семьи программу, которая будет принимать на вход месячный доход мужа и жены и расчитывать сколько им
    нужно отложить на каждую категорию.

    Ваша программа принимает два числа типа float. Целая часть – рубли, а дробная – копейки.

    В качестве результата работы выведите количество рублей и копеек для каждой из категорий в таком формате:
    Отпуск: 10 руб. 5 коп.
    Пропитание и еда: 30 руб. 15 коп.
    Коммунальные платежи: 5 руб. 0 коп.
    Досуг: 10 руб. 11 коп.
    Накопления: 50 руб. 3 коп.

    Решение: Cost_optimization.py