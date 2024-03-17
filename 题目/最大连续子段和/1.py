def max_subarray_sum(a):
    max_sum_whole = a[0]
    max_sum = a[0]
    for i in range(1, len(a)):
        max_sum = max(a[i], max_sum+a[i])
        max_sum_whole = max(max_sum, max_sum_whole)    
    return max_sum_whole

n = int(input())
a = list(map(int, input().split()))
print(max_subarray_sum(a))
