import time
start = time.time()
sum=2
for i in range(3,2000000,2):
    count = 0
    for j in range(3, round(i**(1/2)+1)):
        if i%j==0:
            count += 1
        if count>1:
            break
    if count == 0:
        sum+=i
print(sum, time.time()-start)