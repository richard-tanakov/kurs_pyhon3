import math 

Width,height,depth= float(input()),float(input()),float(input()) 

Width,height,depth=int(math.ceil(Width)),int(math.ceil(height)),int(math.ceil(depth)) #Идет округление в большую сторону.

for i in [Width,height,depth]:
    print(i)

