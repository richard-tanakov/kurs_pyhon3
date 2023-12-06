import json

Data = json.loads(input())

out=set( )
for i in Data:
    num,num1 = (i["chief"]["age"], i["age"])
    out.add(max(num, num1))
print(max(out))