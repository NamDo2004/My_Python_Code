def Max_nums_divisible(x,y):
    max = 0
    for i in x:
        if i % y == 0:
            if i > max:
                max = i
    return max 

a = list(map(int, input().split()))
b = int(input())
c = Max_nums_divisible(a,b)
print(c)