def manhattan_distance(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]+p2[1])

original_point = list(map(int,input().split()))
n = int(input())
points = [list(map(int,input().split())) for _ in range(n)]
