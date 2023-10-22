action = "a"
num = 0
while action[0] != "exit":
    action = str(input()).split()
    if action[0] == "zero":
        num *= 0
    elif action[0] == "result":
        print(num)
    elif action[0] == "add":
        num += int(action[1])
    elif action[0] == "minus":
        num -= int(action[1])
    elif action[0] == "mul":
        num *= int(action[1])
    elif action[0] == "div":
        num //= int(action[1])
