import numpy as np
from PIL import Image
import sys

sys.setrecursionlimit(100000)
# 读取迷宫图片
title = 'maze02'
maze_image = Image.open(f'{title}.png')
maze_pixels = np.array(maze_image)

# 定义颜色值
start_color = [0, 200, 0]  # 绿色
end_color = [255, 0, 0]  # 红色
wall_color = [0, 0, 0]  # 黑色
path_color = [255, 255, 0]  # 黄色

# 获取起点和终点的坐标
start_pos = np.argwhere(np.all(maze_pixels == start_color, axis=-1))[0]
end_pos = np.argwhere(np.all(maze_pixels == end_color, axis=-1))[0]

# 创建一个与迷宫图片相同大小的二维数组，用于表示迷宫的通道和墙壁
maze = np.where(np.all(maze_pixels == wall_color, axis=-1), 0, 1)

# 使用深度优先搜索算法找到从起点到终点的路径
def dfs(maze, pos):
    if np.array_equal(pos,end_pos):
        return True
    x, y = pos
    maze[x, y] = 2  # 标记已经走过的路
    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]  # 上下左右四个邻居
    for neighbor in neighbors:
        nx, ny = neighbor
        if 0 <= nx < maze.shape[0] and 0 <= ny < maze.shape[1] and maze[nx, ny] == 1:
            if dfs(maze, (nx, ny)):
                return True
    maze[x, y] = 0
    return False

# 调用深度优先搜索算法找到路径
dfs(maze, start_pos)

# 将路径标记为黄色
maze_pixels[np.where(maze == 2)] = path_color
maze_pixels[start_pos[0],start_pos[1]] = start_color

# 保存结果图片
result_image = Image.fromarray(maze_pixels)
result_image.save(f'{title}_solution.png')