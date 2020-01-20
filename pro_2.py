fibo = [1, 2]
i=2
sum = 0
while fibo[i-1] <= 4000000:
    fibo.append(fibo[i-1]+fibo[i-2])
    if fibo[i-1] % 2 == 0:
        sum += fibo[i-1]
    i+=1
print(sum)