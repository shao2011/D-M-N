import time
m,n = [int(x) for x in input().split()]
db = [[int(x) for x in input().split()] for i in range(m)]
kq = [['x' for x in range(n)] for i in range(m)]

def so_bom_da_biet(i,j):
    s = 0
    if (i,j)==(0,0):
        if kq[0][1] == 1: s+=1
        if kq[1][0] == 1: s+=1 
        if kq[1][1] == 1: s+=1
    elif (i,j)==(m-1,0):
        if kq[m-2][0] == 1: s+=1
        if kq[m-2][1] == 1: s+=1 
        if kq[m-1][1] == 1: s+=1
    elif (i,j)==(0,n-1):
        if kq[0][n-2] == 1: s+=1
        if kq[1][n-1] == 1: s+=1 
        if kq[1][n-2] == 1: s+=1
    elif (i,j)==(m-1,n-1):
        if kq[m-1][n-2] == 1: s+=1
        if kq[m-2][n-1] == 1: s+=1 
        if kq[m-2][n-2] == 1: s+=1

    elif j==0:
        for e in range(i-1,i+2):
            if kq[e][1]==1: s+=1
        if kq[i-1][j]==1: s+=1
        if kq[i+1][j]==1: s+=1
    elif j==n-1:
        for e in range(i-1,i+2):
            if kq[e][j-1]==1: s+=1
        if kq[i-1][j]==1: s+=1
        if kq[i+1][j]==1: s+=1
    elif i==0:
        for e in range(j-1,j+2):
            if kq[1][e]==1: s+=1
        if kq[0][j-1]==1: s+=1
        if kq[0][j+1]==1: s+=1
    elif i==m-1:
        for e in range(j-1,j+2):
            if kq[m-2][e]==1: s+=1
        if kq[m-1][j-1]==1: s+=1
        if kq[m-1][j+1]==1: s+=1
    
    else:
        for e in range(i-1,i+2):
            for f in range(j-1,j+2):
                if (e,f) != (i,j) and kq[e][f] ==1: s+=1
    return s

def so_o_chua_giai(i,j):
    s = 0
    if (i,j)==(0,0):
        if kq[0][1] == 'x': s+=1
        if kq[1][0] == 'x': s+=1 
        if kq[1][1] == 'x': s+=1
    elif (i,j)==(m-1,0):
        if kq[m-2][0] == 'x': s+=1
        if kq[m-2][1] == 'x': s+=1 
        if kq[m-1][1] == 'x': s+=1
    elif (i,j)==(0,n-1):
        if kq[0][n-2] == 'x': s+=1
        if kq[1][n-1] == 'x': s+=1 
        if kq[1][n-2] == 'x': s+=1
    elif (i,j)==(m-1,n-1):
        if kq[m-1][n-2] == 'x': s+=1
        if kq[m-2][n-1] == 'x': s+=1 
        if kq[m-2][n-2] == 'x': s+=1

    elif j==0:
        for e in range(i-1,i+2):
            if kq[e][1]=='x': s+=1
        if kq[i-1][j]=='x': s+=1
        if kq[i+1][j]=='x': s+=1
    elif j==n-1:
        for e in range(i-1,i+2):
            if kq[e][j-1]=='x': s+=1
        if kq[i-1][j]=='x': s+=1
        if kq[i+1][j]=='x': s+=1
    elif i==0:
        for e in range(j-1,j+2):
            if kq[1][e]=='x': s+=1
        if kq[0][j-1]=='x': s+=1
        if kq[0][j+1]=='x': s+=1
    elif i==m-1:
        for e in range(j-1,j+2):
            if kq[m-2][e]=='x': s+=1
        if kq[m-1][j-1]=='x': s+=1
        if kq[m-1][j+1]=='x': s+=1
    
    else:
        for e in range(i-1,i+2):
            for f in range(j-1,j+2):
                if (e,f) != (i,j) and kq[e][f] =='x': s+=1
    return s

dictt = dict()
def S(i,j):
    p = db[i][j] - so_bom_da_biet(i,j)
    dictt[(i,j)] = [None]
    '''
    print('p:',p)
    print('số bom đã biết:',so_bom_da_biet(i,j))
    print('số ô chưa giải:',so_o_chua_giai(i,j))
    print(so_o_chua_giai == 0 and p == 0)'''
    # p luôn <= so_o_chua_giai --> chọn 1 cách để giải
    # nếu p > so_o_chua_giai --> vô lý
    if p <= so_o_chua_giai(i,j):
        if so_o_chua_giai(i,j)==3:
            if p == 3:
                dictt[(i,j)].append([1,1,1])
            elif p == 0:
                dictt[(i,j)].append([0,0,0])
            elif p == 1:
                dictt[(i,j)].append([1,0,0])
                dictt[(i,j)].append([0,1,0])
                dictt[(i,j)].append([0,0,1])
            else:
                dictt[(i,j)].append([0,1,1])
                dictt[(i,j)].append([1,0,1])
                dictt[(i,j)].append([1,1,0])
        elif so_o_chua_giai(i,j)== 2:
            if p == 2:
                dictt[(i,j)].append([1,1])
            elif p == 1:
                dictt[(i,j)].append([1,0])
                dictt[(i,j)].append([0,1])
            else:
                dictt[(i,j)].append([0,0])
        elif so_o_chua_giai(i,j)==1:
            if p ==1:
                dictt[(i,j)].append(1)
            else:
                dictt[(i,j)].append(0)
    if so_o_chua_giai(i,j) == 0 and p == 0:
        dictt[(i,j)].append('Hop ly')


def gan_gtri_xq(i,j): # chỉ dùng hàm gắn gtri khi dictt[(i,j)][-1] != None và != 'Hop ly'
    if j ==0:
        if i == 0: 
            kq[0][1] =dictt[(i,j)][-1][0]
            kq[1][0] =dictt[(i,j)][-1][1]
            kq[1][1] =dictt[(i,j)][-1][2]
        elif i==1:
            kq[0][0] =dictt[(i,j)][-1][0]
            kq[2][0] =dictt[(i,j)][-1][1]
            kq[2][1] =dictt[(i,j)][-1][2]
        elif i < m-1:
            kq[i+1][j]= dictt[(i,j)][-1][0]
            kq[i+1][j+1]=dictt[(i,j)][-1][1]

    elif j > 0 and j != n-1:
        if i == 0:
            kq[i][j+1] = dictt[(i,j)][-1][0]
            kq[i+1][j+1]=dictt[(i,j)][-1][1]
        elif i < m-1:
            kq[i+1][j+1]=dictt[(i,j)][-1]
    
def go_gtri_xq(i,j): # chỉ dùng hàm gỡ giá trị về x khi quay lui
    if j ==0:
        if i == 0:
            kq[0][1] = 'x'
            kq[1][0] = 'x'
            kq[1][1] = 'x'
        elif i==1:
            kq[0][0] = 'x'
            kq[2][0] = 'x'
            kq[2][1] = 'x'
        elif i < m-1:
            kq[i+1][j]= 'x'
            kq[i+1][j+1]= 'x'

    elif j > 0 and j != n-1:
        if i == 0:
            kq[i][j+1] = 'x'
            kq[i+1][j+1]= 'x'
        elif i < m-1:
            kq[i+1][j+1]= 'x'

seconds = time.time()
i=0
j=0
kd_quay_lui = 'NO'
while j<n:
    while i<m:
        if kd_quay_lui == 'NO':
            S(i,j)
        else: 
            go_gtri_xq(i,j)
        # print((i,j),dictt[(i,j)],kd_quay_lui)
        if dictt[(i,j)][-1] != None and dictt[(i,j)][-1] != 'Hop ly':
            kd_quay_lui = 'NO'
            gan_gtri_xq(i,j)
            if i == m-1:
                i=0
                j+=1
            else:
                i += 1
            
        elif dictt[(i,j)][-1] == None:
            #quay lui
            kd_quay_lui = 'Yes'
            if i==0:
                i = m-1
                j -= 1
            else:
                i -= 1
            dictt[(i,j)].pop()
        elif dictt[(i,j)][-1] == 'Hop ly':
            kd_quay_lui = 'NO'
            if (i,j)==(m-1,n-1):
                i+=1
                j+=1
            elif i == m-1:
                i=0
                j+=1
            else:
                i+=1
        '''for row in kq:
                print(*row)
        print('\n')
print('Kết quả:')'''
seconds_1 = time.time()

for row in kq:
    print(*row)
print('thời gian: ',seconds_1 - seconds)
''' 4 3
3 3 2
3 4 4
5 4 3
2 2 2
'''

''' 10 15
0 3 2 3 3 3 5 3 4 4 5 4 4 4 3
1 4 3 5 5 4 5 4 7 7 7 5 6 6 5
1 4 3 5 4 3 5 4 4 4 4 3 4 5 5 
1 4 2 4 4 5 4 2 4 4 3 2 3 5 4
1 3 2 5 4 4 2 2 3 2 3 3 2 5 2
2 3 2 3 3 5 3 2 4 4 3 4 2 4 1
2 3 2 4 3 3 2 3 4 6 6 5 3 3 1
2 6 4 5 2 4 1 3 3 5 5 5 6 4 3
4 6 5 7 3 5 3 5 5 6 5 4 4 4 3
2 4 4 4 2 3 1 2 2 2 3 3 3 4 2
'''
        

        
            
         

        