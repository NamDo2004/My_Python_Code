def sort_matrix_alternately(matrix, n, start_with_ascending):
    for i in range(n):
        matrix[i].sort(reverse=not start_with_ascending)  # Đảo ngược thứ tự sắp xếp
        start_with_ascending = not start_with_ascending  # Chuyển đổi cho hàng tiếp theo

    return matrix

# Đọc dữ liệu từ đầu vào
n, _ = map(int, input().split())  # Loại bỏ biến m không cần thiết
matrix = [list(map(int, input().split())) for _ in range(n)]
start_with_ascending = bool(int(input()))

# Sắp xếp và in kết quả
sorted_matrix = sort_matrix_alternately(matrix, n, start_with_ascending)
for row in sorted_matrix:
    print(' '.join(map(str, row)))
