def Check(mang, n):
    for i in range(1, n):
        #So sánh phần tử đứng sau có lớn hơn phần tử đứng trước không
        #VD: [1,5,7,9]
        # 5>1
        # 7>5
        # 9>7
        if mang[i] <= mang[i-1]:
         return "KHONG_TANG"
    return "TANG"

a = int(input())
mang_a = list(map(float, input().split()))

b = int(input())
mang_b = list(map(float, input().split()))

print(Check(mang_a, a))
print(Check(mang_b, b))