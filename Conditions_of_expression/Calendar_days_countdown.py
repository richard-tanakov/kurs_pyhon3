"Не использую библиотеки так как тема на if, elif, else"
amount_of_days = int(input())


def conclusion(day):
    if day == 0:
        print(("пн"))
    elif day == 1:
        print("вт")
    elif day == 2:
        print("ср")
    elif day == 3:
        print("чт")
    elif day == 4:
        print("пт")
    elif day == 5:
        print("сб")
    else:
        print("вс")


if amount_of_days >= 7:
    day = amount_of_days % 7
    conclusion(day)
else:
    day = amount_of_days
    conclusion(day)
