#write a python program to print the sum of palindromes and also print list of palindrome

def palindrome(n) :
    s=str(n)
    if s==s[::-1] :
        return 1
    else :
        return 0
    
n,m=map(int,input().split(","))
l1,l2=[],[]
for i in range(n,m+1) :
    flag=palindrome(i)
    if flag==1 :
        l1.append(i)
    if i%2==0 :
        if flag==1 :
            l2.append(i)
print(l1)
print(l2)
            

