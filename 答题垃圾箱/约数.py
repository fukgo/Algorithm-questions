def sum_factors(n):
    result = 0
    i = 1
    while i*i <= n:
        if n % i == 0:
            result += 2  # 找到一个因子 i 和对应的 n//i
        i += 1
    # 如果 n 是完全平方数，那么只计算一个平方根因子
    if i*i == n:
        result -= 1
    return result

def sum_factors_up_to_n(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += sum_factors(i)
    return total_sum

num = int(input("请输入一个数："))
result = sum_factors_up_to_n(num)
print(result)
