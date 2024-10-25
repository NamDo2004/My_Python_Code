def TowerOfHanoi(n,N,T,D):
    if n==1:
        print("Đĩa:",n," di chuyển từ ",N," đến ",D)
        return()
    TowerOfHanoi(n-1,N,D,T)
    print("Đĩa:",n," di chuyển từ ",N," đến ",D)
    TowerOfHanoi(n-1,T,N,D)

n = int(input("Mời nhập số lượng đĩa: "))
TowerOfHanoi(n,'N','T','D')