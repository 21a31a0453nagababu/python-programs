#write a python program to print factorial of given number

def fact(n) :
    if n<1 :
        return 1
    else :
        return n*fact(n-1)



n=int(input())
fact=fact(n)
print(fact)
