num_list = [2,3]
i=1
x=3
while i < 10000:
    n=0
    x+=2
    for j in range(1, round(num_list[i]**(1/2))+1):
        if x%j==0:
            n+=1
    if n==1:
        num_list.append(x)
        i+=1
print(num_list)