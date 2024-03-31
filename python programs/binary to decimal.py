#write a python program to convert binary value to decimal value?
n=int(input())
binary_val=n
decimal_val=0
base=1
while n>0 :
    rem=n%10
    decimal_val=decimal_val+rem*base
    n=n//10
    base=base*2
print(decimal_val)
