n=int(input())
d={}
for i in range(n) :
    key=input("Enter a key")
    value=input()
    d[key]=value
print(d)
m=int(input("Enter a search items :"))
for i in  range(m) :
    s=input()
    if s in d.values():
        for i in d.keys() :
            if d[i]==s :
                print(i,d[i])
    else : 
        print("Not found")
