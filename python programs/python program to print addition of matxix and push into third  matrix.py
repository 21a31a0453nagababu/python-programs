#write a python program to print addition of matrix

r,c=map(int,input().split())
l=[0]*r
l1=[]
l2=[]
for i in range(r) :
    l[i]=[0]*c
for i in range(r) :
    l1.append(tuple(map(int,input().split())))
    l2.append(tuple(map(int,input().split())))
for i in range(r) :
    for j in range(c) :
        l[i][j]=l1[i][j]+l2[i][j]
        
for i in l:
    print(i)
