a=int(input())
al=[]
for i in range(1, round(a**(1/2))):
    if a%i==0:
        al.append(i)
        al.append(int(a/i))
al.sort()
print(al)

for i in range(len(al)):
    n=0
    for j in range(1, round(al[i]**(1/2))):
        if al[i]%j==0:
            n+=1
    if n==1:
        max = al[i]

print(max)