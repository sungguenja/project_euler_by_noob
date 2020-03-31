X=[0]*10001
for i in range(2,10001):
    now_sum=0
    for j in range(1,i-1):
        if i%j==0:
            now_sum+=j
    X[i]=now_sum
now_sum=0
for i in range(10001):
    if X[i]<=10000 and i == X[X[i]] and X[i] != i:
        now_sum += i
        print(X[i],X[X[i]],i)
print(now_sum)