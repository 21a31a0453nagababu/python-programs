#write a python program to print last column sum
r,c=map(int,input().split())
l=[]
sum=0
for i in range(r) :
    l.append(tuple(map(int,input().split())))

for i in l :
    sum=sum+i[c-1]
print(sum)
    
