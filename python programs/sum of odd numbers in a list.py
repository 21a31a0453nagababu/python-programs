#write a python program to print sum of odd in a list
n,m=map(int,input().split())
l=[i for i in range(n,m+1) if i%2!=0]
print(sum(l))
