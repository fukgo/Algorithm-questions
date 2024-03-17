from collections import deque

# 输入字符矩阵
matrix = []
for _ in range(3):
    row = input().strip()
    matrix.append(row)

# 转换坐标表示法
def to_coordinates(coord):
    return (coord // 3, coord % 3)

# 转换字符到坐标的映射
char_to_coords = {}
for i in range(3):
    for j in range(3):
        char_to_coords[matrix[i][j]] = (i, j)

# 定义移动方向
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 广度优先搜索找到最短路径
def shortest_path(start, end):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path

        if current not in visited:
            visited.add(current)
            for direction in directions:
                next_x, next_y = to_coordinates(current)
                next_x += direction[0]
                next_y += direction[1]
                if 0 <= next_x < 3 and 0 <= next_y < 3:
                    next_pos = next_x * 3 + next_y
                    queue.append((next_pos, path + [to_coordinates(next_pos)]))

# 找到最短路径顺序
password = "0123456789"
start = char_to_coords[password[0]]
end = char_to_coords[password[len(password) - 1]]
path_order = shortest_path(start[0] * 3 + start[1], end[0] * 3 + end[1])

# 输出结果
output = " -> ".join([f"({x+1},{y+1})" for x, y in path_order])
print(output)
