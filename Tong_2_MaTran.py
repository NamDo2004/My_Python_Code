#Nhập ma trận thứ nhất
n1, m1 = map(int, input().split())
x = []
for i in range(n1):
    row_x = list(map(int, input().split()))
    x.append(row_x)
#Nhập ma trận thứ hai
n2, m2 = map(int, input().split())
y = []
for i in range(n2):
    row_y = list(map(int, input().split()))
    y.append(row_y)
#Kiểm tra xem hàng và cột của hai ma trận có bằng nhau hay không
if n1!=n2 or m1!=m2:
    print("Du lieu vao sai")
else:
    #Khai báo ma trận tổng kích thước n1, m1 với các phần tử là 0
    s = [[0]*m1 for _ in range(n1)]
    for i in range(n1):
        for j in range(m1):
            #Tính tổng hai ma trận
            s[i][j] = x[i][j] + y[i][j]
    #In kết quả
    print("Ma tran tong")
    for i in range(n1):
        for j in range(m1):
            print(s[i][j], end=" ")
        print()


