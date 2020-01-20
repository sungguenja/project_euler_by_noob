pal = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None}
c=1

for i in range(100,1000):
    for j in range(100,1000):
        a=i*j
        b=a
        if a<100000:
            for n in range(5):
                pal[n] = a%10
                a = int(a/10)
            if pal[0] == pal[4] and pal[1] == pal[3] and b > c:
                c=b
        if a >= 100000:
            for n in range(6):
                pal[n] = a%10
                a = int(a/10)
            if pal[0] == pal[5] and pal[1] == pal[4] and pal[2] == pal[3] and b > c:
                c=b

print(c)