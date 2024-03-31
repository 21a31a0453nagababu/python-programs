import math
m,c=map(int,input().split(","))
if m>c :
    remain=m-c
    result=remain/4
    print(math.ceil(result))
else :
    print(0)
