def Remove_Digit_To_Get_Smalles(m, n):
    m_str = str(m) #chuyển m thành dạng chuỗi để tách các chữ số
    for i in range(len(m_str)):
        """
        m_str: chuỗi ban đầu được chuyển từ số m sang
        m_str[:i]: cắt chuỗi m_str từ vị trí đầu đến vị trí i-1
        m_str[i+1:]: cắt chuỗi m_str từ vị trí i+1 đến hết chuỗi
        Sau đó nối 2 đoạn chuỗi vừa cắt lại với nhau để tạo ra chuỗi p_str
        """
        p_str = m_str[:i] + m_str[i+1:]
        p = int(p_str)
        if p % n == 0:
            return p
    return "impossible"

m, n = map(int, input().split())
result = Remove_Digit_To_Get_Smalles(m,n)
print(result)
