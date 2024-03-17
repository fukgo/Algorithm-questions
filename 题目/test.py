from collections import defaultdict
def longestPalindrome(s):
    d = defaultdict(int)
    for i in s:
        if not d[i]:
            d[i]=1
        else:
            d[i]+=1

    res = 0
    one = 0
    for _,val in d.items():
        if val%2==0:
            print(val)
            res += val
        if val % 2 != 0:
            print(val)
            res += round(val / 2)
            o =1

    if res%2==0:
        res += o
    return res



s="abccccdd"
print(longestPalindrome(s))