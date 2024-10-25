def Find_Strong_Num(x):
    if x == 0:
        print("false")
        return
    s = 0
    num = x
    while x > 0:
        #Lấy từng số từ input
        digit = x % 10
        fact = 1
        #dùng vòng lặp tính giai thừa
        for i in range (1, digit + 1):
            fact = fact * i
        #Cập nhật lại sum
        s = s + fact
        #Giảm số nhập vào 10 lần
        x = x // 10
    #Kiểm tra sum == x hay không
    if(s==num): print("true")
    else: print("false")

x = int(input())
y = Find_Strong_Num(x)
