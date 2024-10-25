"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
"""
def CheckPrime(a):
    if a <= 1: return False
    for c in range(2, a):
        if a%c == 0: return False
    return True

a = int(input("Moi nhap so bat ki: "))
if CheckPrime(a): print(str(a) + " la mot so nguyen to")
else: print(str(a) + " khong phai la mot so nguyen to")



    