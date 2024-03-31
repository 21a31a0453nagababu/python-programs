n,s=map(int,input().split(","))
wantpieces=n*s
each_pizza=4
if wantpieces%4==0:
    np=wantpieces//4
else :
    np=(wantpieces//4)+1
print(np)
    
    
