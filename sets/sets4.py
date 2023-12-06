list_1 = list(input().split())
set_1 = set(list_1)
dict_1 = {i: list_1.count(i) for i in set_1}
dict_sort = list(sorted(dict_1.items()))
for key, values in dict_sort:
    print("{0} {1}".format(key, values))
