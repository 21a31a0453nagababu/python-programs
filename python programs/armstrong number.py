n=int(input())
order=len(str(n))
sum=0
for i in range(n) :
    if n>0 :
        digit=n%10
        sum+=digit**order
        n//=10
       if (str(sum)==str(n)) :
             print("Armstrong")
