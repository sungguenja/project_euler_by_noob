num_sum = 0
for i in range(100):
    num_input = int(input()[:13])
    num_sum += num_input
num_site = list(str(num_sum))[:10]
print(''.join(num_site))