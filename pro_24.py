visit = [0]*10
case = 0
def find(now=''):
    global case
    if len(now)==10:
        case+=1
        return
    
    if case==1000000:
        print(now,case)
        return now

    for i in range(10):
        if visit[i]==0:
            visit[i]=1
            find(now+str(i))
            visit[i]=0
ans = find()
print(ans)