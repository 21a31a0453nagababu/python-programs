#write a program to check whether is prime number or not

n=int(input())
count=0

for val in range(1,n+1) :
    if val>1 :
        for i in range(2,n+1) :
            if (val%i==0) :
                break
        else :
            print(val,end=" ")


            
