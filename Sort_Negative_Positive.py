def Sort_Array(arr):
    negative = [x for x in arr if x < 0]
    positive = [x for x in arr if x >= 0]
    
    negative.sort(reverse=True)
    positive.sort()

    return negative + positive

a = list(map(int, input().split()))
result = Sort_Array(a)

print(" ".join(map(str, result)))
