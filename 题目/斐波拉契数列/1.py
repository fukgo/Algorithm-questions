"""
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765
"""
# m为第m项
class Solution:
    def uniquePaths(self, m):
        if m == 1 or m == 2:
            return 1
        else:
            return self.uniquePaths(m-1)+self.uniquePaths(m-2)

x = Solution()
print(x.uniquePaths(40))
