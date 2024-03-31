string=input()
n=input()
for i in range(len(string)):
    if int(string[i])<=int(n) :
        s=string[:i]+n+string[i:]
        print(s)
        break
else :
    print(s+d)
    
        
