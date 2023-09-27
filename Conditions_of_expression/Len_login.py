login = input()
password = input()


def checking_numbers(password, login):
    if (login.isdigit() == True) and (password.isdigit() == True):
        print(
            len(str(login)) > 4
            and len(str(password)) > 8
            and not int(login) == int(password)
        )
    else:
        login = len(str(login))
        password = len(str(password))
        print(login > 4 and password > 8 and not login == password)


checking_numbers(password, login)
