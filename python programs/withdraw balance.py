withdraw=int(input())
balance=int(input())
condition=(balance>withdraw) and (withdraw%5==0)
if condition :
    print(balance-withdraw)
else :
    print(balance)
a,b=map(int,input().split(","))
if a>b:
    print("a is greater")
else :
    print("b is greater")
