class NV:
    def __init__(self, ten, ma, hsl, pc):
        self.ten = ten
        self.ma = ma
        self.hsl = hsl
        self.pc = pc
    def luong(self):
        return self.hsl * 2000000 + self.pc
    
n = int(input())
#Tạo mảng m
m = []
for i in range(n):
    ten, ma, hsl, pc = input().split()
    hsl = float(hsl)
    pc = int(pc)
    nhan_vien = NV(ten, ma, hsl, pc)
    m.append(nhan_vien)

#Tìm nhân viên lương max
nv_luong_max = max(m, key=lambda x: x.luong())

print("Nhan vien co luong cao nhat")
print("{} {} {:.2f} {} {:.2f}".format(
    nv_luong_max.ma,
    nv_luong_max.ten,
    nv_luong_max.hsl,
    nv_luong_max.pc,
    nv_luong_max.luong()
))
