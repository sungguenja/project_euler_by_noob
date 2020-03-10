max_num=0
def triangle(N,go=0,depth=1,su=75):
    global max_num
    
    if depth==N and su>max_num:
        max_num=su
        return
    
    for i in range(go,go+2):
        if depth < N and visit[depth][i] == 0:
            visit[depth][i] = 1
            triangle(N,i,depth+1,su+num_list[depth][i])
            visit[depth][i] = 0

N=15
num_list = [list(map(int,input().split())) for _ in range(N)]
visit = [[0]*(i+1) for i in range(N)]
triangle(N)
print(max_num)