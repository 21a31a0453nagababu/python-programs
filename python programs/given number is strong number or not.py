#write a python program to print thegiven number is strong number
def func(n) :
    x,sum=n,0
    while n>0 :
        digit=n%10
        fact=1
        for i in range(1,digit+1) :
            fact*=i
        sum+=fact
        n//=10
    if sum==x :
        return "STRONG NUMBER"
    else:
        return "NOT STRONG NUMBER"
n=int(input())
result=func(n)
print(result)








