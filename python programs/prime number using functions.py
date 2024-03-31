#write a python program to print prime numbers in a range using function


def func(m,n) :
    
    for val in range(m,n+1) :
        if val>0 :
            for i in range(2,val) :
                if val%i==0 :
                    break
            else :
              print(val)
            






m=int(input())
n=int(input())
result=func(m,n)
