def letterCombinations(digits):
    map = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    n = len(digits)
    if n == 0:
        return []
    ans = []
    path = [''] * n
    def dfs(i):
        print("i=", i)
        if i == n:
            ans.append(''.join(path))
            print(ans)
            return
        for j in map[int(digits[i])]:
            print('int(digits[i])',int(digits[i]))
            path[i] = j
            print(path)
            dfs(i + 1)
    dfs(0)
    return ans
x = letterCombinations('23')
print(x)