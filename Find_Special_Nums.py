"""Định nghĩa Hàm find_special_elements(matrix):

matrix: Biến này chứa ma trận mà bạn muốn tìm các phần tử đặc biệt.
Kiểm tra Ma trận Rỗng:

if not matrix or not matrix[0]: Kiểm tra xem ma trận có rỗng không. Nếu rỗng, hàm sẽ trả về một list rỗng.
Lấy Kích thước của Ma trận:

rows, cols = len(matrix), len(matrix[0]): Lấy số hàng (rows) và số cột (cols) của ma trận.
Tìm Các Phần Tử Trong Hàng Đầu Tiên:

row_set = set(matrix[0]): Tạo một set từ hàng đầu tiên của ma trận. Set này sẽ được sử dụng để tìm giao điểm với các hàng khác.
Tìm Giao Điểm của Các Hàng:

for i in range(1, rows): Lặp qua mỗi hàng, bắt đầu từ hàng thứ hai.
row_set &= set(matrix[i]): Tìm giao điểm của set hiện tại với set của hàng hiện tại. Điều này giúp lọc ra các phần tử xuất hiện trong mọi hàng.
Tìm Phần Tử Trong Mọi Cột:

col_set = set(): Khởi tạo một set rỗng cho các cột.
for j in range(cols): Lặp qua mỗi cột.
col_elements = set(matrix[i][j] for i in range(rows)): Tạo một set từ các phần tử trong cột hiện tại.
col_set |= col_elements: Thêm các phần tử của cột vào col_set.
Tìm Giao Điểm giữa Hàng và Cột:

return list(row_set & col_set): Trả về giao điểm của các phần tử trong hàng và cột dưới dạng list.
Nhập Dữ Liệu từ Người Dùng:

n, m = map(int, input().split()): Nhập số hàng và số cột từ người dùng.
matrix = [list(map(int, input().split())) for _ in range(n)]: Nhập từng hàng của ma trận.
Gọi Hàm và In Kết Quả:

special_elements = find_special_elements(matrix): Gọi hàm với ma trận vừa nhập.
print(" ".join(map(str, special_elements))): In các phần tử đặc biệt, chuyển chúng thành chuỗi và nối với nhau bằng dấu cách.
"""

def Find_Special(matrix):
    #Kiếm tra ma trận rỗng
    if not matrix or not matrix[0]:
        return []
    #Lấy kích thước ma trận
    rows, cols = len(matrix), len(matrix[0])
    #row_set là tập hợp các phần tử hàng đầu tiên
    row_set = set(matrix[0])
    #Duyệt qua từng mảng còn lại và lấy giao của row_set với các phần tử từng hàng
    for i in range(1, rows):
        row_set &= set(matrix[i])
    #Tương tự với các cột, khởi tạo col_set và duyệt từng cột
    col_set = set()
    #duyệt qua từng mảng còn lại và lấy giao của row_set với các phần tử từng cột
    #for j in range(cols): duyệt từ cột 0 đến cột cols-1
    #col_elements = set(matrix[i][j] for i in range(rows)):
    #Tạo ra một set tên là col_elements, bao gồm các phần tử của cột j
    #matrix[i][j]: truy xuất phần tử ở hàng i, cột j của ma trận
    #Duyệt từ hàng 0 đến hàng rows-1 để lấy tất cả các phần tử của cột j
    #col_set |= col_elements: Hợp các phần tử vào col_set
    for j in range(cols):
        col_elements = set(matrix[i][j] for i in range(rows))
        col_set |= col_elements
    return  list(row_set & col_set)

n, m = map(int, input().split())
#nhập dư liệu cho mỗi hàng
matrix = [list(map(int, input().split())) for _ in range(n)]
Result = Find_Special(matrix)
print(" ".join(map(str, Result)))

    

    
