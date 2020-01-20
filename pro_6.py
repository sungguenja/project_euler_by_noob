sum=0
for i in range(1,101):
    for j in range(i,101):
        if i!=j:
            sum+=2*i*j
        else:
            m=1
print(sum)