max_num = [0,0]
for i in range(2,1000000):
    z=1
    su = i
    while su > 1:
        if su % 2 == 0:
            su = su//2
            z+=1
        else:
            su = 3*su+1
            z+=1
    if z>max_num[1]:
        max_num = [i,z]
print(max_num)