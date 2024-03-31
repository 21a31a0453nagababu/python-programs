#write a python program count of vowels in even and odd position

s=input()
ev,oc=0,0
for i in range(len(s)) :
    if i%2==0 :
        ev+=1
    elif i%2!=0 :
        oc+=1
    

