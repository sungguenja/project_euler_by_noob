longest_len = -1
longest_num = -1
for i in range(1,1000):
    now_i = str(round(1/i,1000))[2:]
    for j in range(len(now_i)//2):
        trigger = False
        for k in range(j+1,len(now_i)//2):
            if now_i[j:k] == now_i[k+1:2*k-j+1]:
                trigger = True
                if longest_len<k-j:
                    longest_len=k-j
                    longest_num=i
                    print(now_i[j:k],1/i)
                    break
            if trigger:
                break
print(longest_len,longest_num)