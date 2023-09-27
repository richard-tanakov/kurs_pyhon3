n1, n2, n3, n4 = [int(i) for i in input().split(".")]


def out(n1, n2, n3, n4):
    if (n1 == 0) and (n2 == 0) and (n3 == 0) and (n4 == 0):
        print("False")
    elif (n1 == 255) and (n2 == 255) and (n3 == 255) and (n4 == 255):
        print("False")
    else:
        print("True")


if (n1 > 255) or (n2 > 255) or (n3 > 255) or (n4 > 255):
    print("False")
else:
    out(n1, n2, n3, n4)
