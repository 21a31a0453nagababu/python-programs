#write a python program to print which are not divisible by 6,7,8 in given range?


n=int(input())

for i in range(1,n+1) :
    if i%6!=0 and i%7!=0 and i%8!=0 :
        print(i,end=" ")
