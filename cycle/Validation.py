correct_list = [
    "0.0.0.0",
    "128.0.0.0",
    "192.0.0.0",
    "224.0.0.0",
    "240.0.0.0",
    "248.0.0.0",
    "252.0.0.0",
    "254.0.0.0",
    "255.0.0.0",
    "255.128.0.0",
    "255.192.0.0",
    "255.224.0.0",
    "255.240.0.0",
    "255.248.0.0",
    "255.252.0.0",
    "255.254.0.0",
    "255.255.0.0",
    "255.255.128.0",
    "255.255.192.0",
    "255.255.224.0",
    "255.255.240.0",
    "255.255.248.0",
    "255.255.252.0",
    "255.255.254.0",
    "255.255.255.0",
    "255.255.255.128",
    "255.255.255.192",
    "255.255.255.224",
    "255.255.255.240",
    "255.255.255.248",
    "255.255.255.252",
    "255.255.255.254",
    "255.255.255.255",
]
num1, num2, num3, num4 = [int(i) for i in input().split(".")]
adress = str(input())


def check_validations(ip_adress, mask):
    if (ip_adress == False) or (mask == False):
        print("Валидация не пройдена")
    else:
        #слияние ip и маски
        mask1, mask2, mask3, mask4 = [int(i) for i in adress.split(".")]
        out1 = str(num1 & mask1)
        out2 = str(num2 & mask2)
        out3 = str(num3 & mask3)
        out4 = str(num4 & mask4)
        print(out1,out2,out3,out4,sep='.')

""" Проверка маски на корректоность"""
score = 0
for i in correct_list:
    if str(i) == adress:
        score += 1
if score == 1:
    mask = True
else:
    mask = False

""" Проверка ip адреса на корректоность"""


def out_ip(num1, num2, num3, num4):
    if num1 > 255 or num2 > 255 or num3 > 255 or num4 > 255:
        ip_adress = False
    elif num1 == 0 and num2 == 0 and num3 == 0 and num4 == 0:
        ip_adress = False
    elif num1 == 255 and num2 == 255 and num3 == 255 and num4 == 255:
        ip_adress = False
    else:
        ip_adress = True

    check_validations(ip_adress, mask)


out_ip(num1, num2, num3, num4)
