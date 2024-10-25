import numpy as np
_A = [[1,2,3],[4,5,6],[7,8,9]]
_B = [7,9,21]
A = np.array(_A)
B = np.array(_B)
print(A)
#Lấy phần từ hàng 1 cột 2
print("a[0,1]:", A[0,1])
#Lấy tất cả phần tử hàng 2
print("a[1,:]:", A[1,:])
#Lấy tất cả phần tử hàng 1
print("a[0,:]:", A[0,:])
#Lấy tất cả phần tử cột 1
print("a[:,0]:", A[:,0])
#Cộng hai ma trận
print('A + B: \n', A+B)
#Trừ hai ma trận
print('A - B: \n', A-B)
#===================================================
#KHÔNG THỂ CỘNG TRỪ HAI MA TRẬN KHÔNG CÙNG KÍCH THƯỚC
#===================================================
print("A * B: \n", A.dot(B))
print("A * B: \n", A@B)

#Identity matrix là ma trận có số 1 trên dường chéo
_C = np.eye(10)
print(_C)