Y = []
for _ in range(20):
    X = []
    X = list(map(int, input().split()))
    Y.append(X)

muti_save=1
for i in range(20):
    for j in range(17):
        muti = 1
        muti_list=[]
        muti_list.extend([Y[i][j],Y[i][j+1],Y[i][j+2],Y[i][j+3]])
        if 0 in muti_list:
            continue
        muti = muti_list[0]*muti_list[1]*muti_list[2]*muti_list[3]
        if muti_save < muti:
            muti_save = muti
for i in range(17):
    for j in range(20):
        muti = 1
        muti_list=[]
        muti_list.extend([Y[i][j],Y[i+1][j],Y[i+2][j],Y[i+3][j]])
        if 0 in muti_list:
            continue
        muti = muti_list[0]*muti_list[1]*muti_list[2]*muti_list[3]
        if muti_save < muti:
            muti_save = muti
for i in range(17):
    for j in range(17):
        muti = 1
        muti_list=[]
        muti_list.extend([Y[i][j],Y[i+1][j+1],Y[i+2][j+2],Y[i+3][j+3]])
        if 0 in muti_list:
            continue
        muti = muti_list[0]*muti_list[1]*muti_list[2]*muti_list[3]
        if muti_save < muti:
            muti_save = muti
for i in range(17):
    for j in range(3,20):
        muti = 1
        muti_list=[]
        muti_list.extend([Y[i+3][j-3],Y[i+2][j-2],Y[i+1][j-1],Y[i][j]])
        if 0 in muti_list:
            continue
        muti = muti_list[0]*muti_list[1]*muti_list[2]*muti_list[3]
        if muti_save < muti:
            muti_save = muti
print(muti_save)