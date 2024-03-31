#write a python program to print armstrong number in range of number using function?


def func(m,n) :
    
    for i in range(m,n+1) :
        sum=0
        x=i
        while i>0 :
            digit=i%10
            sum=sum+digit**3
            i//=10
        if sum==x :
            print(x)
  




m=int(input())
n=int(input())
result=func(m,n)

