def sxep_XenKe(n, a, ascending):
    for i in range(n):
        a[i].sort(reverse=not ascending)
        ascending = not ascending
    return a
#Input
n, _ = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ascending = bool(int(input()))
#Sxep va in
a_sorted = sxep_XenKe(n, a, ascending)
for i in a_sorted:
    print(' '.join(map(str, i)))