
    
def L(nums, i):
    '''找出从索引 i 开始的最长递增子序列的长度。'''
    if i == len(nums)-1:
        return 1

    max_len = 1
    for j in range(i+1, len(nums)):
        if nums[j] > nums[i]:
            max_len = max(L(nums, j)+1, max_len)
    return max_len

def L_upgrade(nums, i):
    '''找出 nums 的最长递增子序列的长度。'''

    meno = {} # 记忆化搜索
    if i in meno:
        return meno[i]

    if i == len(nums)-1:
        return 1
    
    max_len = 1
    for i in range(len(nums)):
        max_len = max(L(nums, i), max_len)
    return max_len

def L_dp(nums):
    L = [1] * len(nums)
    length = len(nums)
    for i in reversed(range(length)):
        for j in range(i+1, length):
            if nums[j] > nums[i]:
                L[i] = max(L[i], 1+L[j])
    return max(L)