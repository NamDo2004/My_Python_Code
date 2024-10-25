import math
a, b, c = map(int, input().split())
if a + b <= c or b + c <= a or a + c <= b:
    print("DL Sai")
else:
    c = a + b + c 
    p = c/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Dien tich tam giac: {:.2f}".format(s))
    print("Chu vi tam giac: {:.2f}".format(c))