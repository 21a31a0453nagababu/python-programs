m=int(input())
n=int(input())
count=0


for i in range(m,n+1) :
    for a in range(2,i+1) :
        if (i%a==0) :
            count=count+1
            break
if (count==0 and a!=1) :
    print(a)
else :
    print("none")
    
    
    
    

        
