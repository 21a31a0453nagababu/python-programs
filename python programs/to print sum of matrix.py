#write a python program to print sum of matrix?

r,c=int(input()),int(input())
l=[]
sum=0
for i in range(r) :
    l.append(list(map(int,input().split())))
    

for j in l :
    for k in j :
        sum+=k
print(sum)
        
    
             
                  

                  
                  
                  
                
