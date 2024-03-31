#write a python program to print n natural numbers

def recursion(n) :
    if n<1 :
        return 1
    else :
        recursion(n-1)
        print(n)
       

n=int(input())
recursion(n)
