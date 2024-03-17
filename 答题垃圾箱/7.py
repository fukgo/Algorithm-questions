def su(n):
    count = 1
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            power = 0
            while n % factor == 0:
                n //= factor
                power += 1
            count *= (power + 1) 
        factor += 1 if factor == 2 else 2
    if n > 1:
        count *= 2
    return count
n = int(input())
s = 0
for i in range(1, n+1):
    s+=su(i)
print(s)
["a","b","c","d"]
["d","c","b","a"]
