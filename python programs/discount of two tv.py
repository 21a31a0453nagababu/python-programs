tv1,tv2,d1,d2=map(int,input().split(","))
condition1=(d1/tv1)*100
condition2=(d2/tv2)*100

price_tv1=(tv1-condition1)
price_tv2=(tv2-condition2)

if price_tv1<price_tv2 :
    print("tv1")
elif price_tv1>price_tv2 :
    print("tv2")
else :
    print("Any")
