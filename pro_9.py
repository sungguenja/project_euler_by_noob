a=[]
for i in range(1,1000):
    for j in range(1, 1000-i):
        k = 1000 - i -j
        if i*j==500000-1000*k:
            z,x,c = i,j,k
            a.append([z,x,c])
print(z*x*c)