r,c=int(input()),int(input())
l=[]
product=1
for i in range(r) :
    l.append(list(map(int,input().split())))

for j in l :
    for k in j :
        product*=k
print(product)
