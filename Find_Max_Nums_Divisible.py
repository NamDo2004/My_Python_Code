def Find_Max_Nums_Divisible(numbers, divisor):
    max_nums = None
    for num in numbers:
        if num % divisor == 0:
            if max_nums is None or num > max_nums:
                max_nums = num
    return max_nums if max_nums is not None else 0

a = list(map(int, input().split()))
b = int(input())
result = Find_Max_Nums_Divisible(a,b)
print(result)