#Nhap ma tran a
n = int(input())
a = [[0] * 100 for _ in range(100)] #Khoi tao kich thuoc ma tran phu hop
for i in range(n):
    a[i] = list(map(int, input().split()))

#Nhap ma tran b
m = int(input())
b = [[0] * 100 for _ in range(100)]
for i in range(m):
    b[i] = list(map(int, input().split()))

#kiem tra doi xung
flag1, flag2 = 0, 0

for i in range(n):
    for j in range(n):
        if a[j][i] != a[i][j]:
            flag1 += 1

for i in range(m):
    for j in range(m):
        if b[j][i] != b[i][j]:
            flag2 += 1

#Xuat ket qua
if n > 0:
    if flag1 != 0:
        print("Ma tran 1: Khong doi xung")
    else:
        print("Ma tran 1: Co doi xung")

if m > 0:
    if flag2 != 0:
        print("Ma tran 2: Khong doi xung")
    else:
        print("Ma tran 2: Co doi xung")