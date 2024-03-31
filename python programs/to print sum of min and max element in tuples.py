#write a python program to print a sum of matrix in a tuple?

r,c=int(input()),int(input())
l=[]
for i in range(r) :
    l.append(tuple(map(int,input().split())))
min,max=1000,0
for j in l :
    for k in j :
        if k>max :
            max=k
        if k<min :
            min=k
print(max+min)
            
            
        
