n=0
a=2520
while n==0:
    if a%19==0 and a%18==0 and a%17==0 and a%16==0 and a%15==0 and a%14==0 and a%13==0 and a%12==0 and a%11==0:
        n=1
    else:
        n=0
        a+=20

print(a)