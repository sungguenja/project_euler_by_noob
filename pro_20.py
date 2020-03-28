su=1
for i in range(1,101):
    su*=i
    while su%10 == 0:
        su = su//10
print(su)
num = 0
while su>=1:
    num += su%10
    su = su//10
print(num)