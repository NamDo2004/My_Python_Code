import math
a = int(input())
b = int(input())
c = int(input())
if a+b<=c or b+c<=a or a+c<=b:
    print("DL Sai")
else:
    p = (a+b+c)/2
    ChuVi = p*2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    dien_tich = round(s,2)
    chu_vi = round(ChuVi, 2)
    print("Dien tich tam giac:",str(dien_tich))
    print("Chu vi tam giac:",str(chu_vi))
