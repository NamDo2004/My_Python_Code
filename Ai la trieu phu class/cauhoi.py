# cauhoi.py
class Question:
    def __init__(self, content, options, correct_answer):
        self.content = content
        self.options = options
        self.correct_answer = correct_answer

# Danh sách câu hỏi
questions = [
    Question("Python ra đời năm nào?", ["1990", "1991", "1992", "1993"], 2),  # Đáp án là 1991
    Question("Đâu là một loại hình chợ tạm tự phát thường xuất hiện trong các khu dân cư?",
             ["Ếch", "Cóc", "Thằn lằn", "Nhái"], 2),  # Đáp án là Cóc
    Question("Đâu là tên một loại bánh nổi tiếng ở Huế?", ["Khoái", "Thích", "Vui", "Sướng"], 1),  # Đáp án là Khoái
    Question("Tượng đài Chiến thắng Điện Biên Phủ được dựng trên ngọn đồi nào?", ["D1", "C1", "A1", "E1"], 1),  # Đáp án là D1
    Question("Màu chủ đạo của tờ tiền polymer mệnh giá 500.000 đồng là màu nào?", ["Đỏ", "Xanh", "Vàng", "Tím"], 2),  # Đáp án là Xanh
]
