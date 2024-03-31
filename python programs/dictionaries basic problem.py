#Write a python program to print dictionaries  of key value pair?
n=int(input())
d={}
for i in range(n) :
    key=input("Enter a key:")
    value=input("Enter a value:")
    d[key]=value
print(d)

