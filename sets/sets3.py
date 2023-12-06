required = set(input())
optional = set(input())
user_data = set(input())
if optional & user_data | required == user_data:
    print(True)
else:
    print(False)
