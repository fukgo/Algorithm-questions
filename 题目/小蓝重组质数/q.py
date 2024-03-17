from itertools import permutations
import math
def is_prime(num):
    if num <  2:
        return False
    for i in range(2, math.int(num) + 1):
        if num % i == 0:
            return False
    return True

def main():
    n = str(input())
    nums = 0
    perms = [int(''.join(p)) for p in permutations(n)]
    for p in perms:
        if is_prime(p):
            nums += 1
    print(nums)

if __name__ == '__main__':
    main()


    






