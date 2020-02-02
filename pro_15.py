#i think it is problem about combination. 40 0 and i change 20 0 to 1
# arr = [0]*40
# n=len(arr)
# count = 0
# for i in range(2**20 -1, 2**40 - 2**(19) + 1):
#     C=list(bin(i)[2:])
#     if C.count('1') != 20:
#         continue
#     for j in range(n):
#         if i&(1<<j):
#             count += 1
# print(count//20)

# and other idea is checking 1 by 1 root
N=int(input())
grid = [[1]*N]
for i in range(1,N):
    NX =[1]
    for j in range(1,N):
        NX.append(NX[j-1]+grid[i-1][j])
    grid.append(NX)
print(grid[N-1][N-1])