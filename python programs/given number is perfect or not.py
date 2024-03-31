n=int(input())
count=0
for i in range(1,n+1) :
    if (n%i==0) :
        count=count+i
if (count==n):
    print( str(n)+" is perfect")
else :
    print(str(n)+" is NOT PERFECT")
    
