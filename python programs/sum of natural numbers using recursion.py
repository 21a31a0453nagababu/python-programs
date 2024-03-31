#write a python program to print sum of natural numbers
def recursion(n) :
    if n<1 :
        return 1
    else :
        
        return n+recursion(n-1)
n=int(input())
sum=recursion(n)
print(sum)
