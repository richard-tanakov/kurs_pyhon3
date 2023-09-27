(
    str1,
    str2,
    str3,
) = (
    str(input()),
    str(input()),
    str(input()),
)
if len(str1) == len(str2) and (len(str2) != len(str3)):
    print(str2)
elif (len(str1) == len(str3)) or (len(str2) == len(str3)):
    print(str3)
else:
    print(min(str1, str2, str3, key=len))  # Вывод самой минимальной строки.
