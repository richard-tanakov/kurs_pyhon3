string=str(input())
string_score=len(string)

print(string[1]*4)
print(string[string_score-2:]+'!')
print(string[0:string_score-3])
print(string,string[::-1],sep='')
print(string[1::2])
print(string[0::2])