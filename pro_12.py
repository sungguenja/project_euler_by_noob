a=0
n=1
z=True
while z:
    a=n*(n+1)//2
    n+=1
    x=[1]
    for i in range(2,round(a**(1/2))):
        if a%i==0:
            x.append(i)
        if len(x)>=250:
            z=False
            break
print(a,n,x)