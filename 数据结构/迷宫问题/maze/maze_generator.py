from PIL import Image
import sys
import random

sys.setrecursionlimit(100000)
# 定义迷宫的尺寸
maze_width = 100
maze_height = 100

# 创建一个空白的迷宫图像，初始时所有像素都是黑色的（代表墙体）
maze_image = Image.new("RGB", (maze_width, maze_height), "black")
maze_pixels = maze_image.load()

# 定义通道和墙体的颜色
channel_color = (255, 255, 255)  # 白色
wall_color = (0, 0, 0)  # 黑色

# 定义起点和终点的颜色
start_color = (0, 200, 0)  # 绿色
end_color = (255, 0, 0)  # 红色

# 生成迷宫函数
def generate_maze(x, y):
    # 终止条件：若当前位置已经在边界上，则返回
    if x == 0 or y == 0 or x == maze_width - 1 or y == maze_height - 1:
        return
    
    # 将当前位置设置为通道
    maze_pixels[x, y] = channel_color
    
    # 在四个方向上随机选择一个未访问的相邻位置
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= maze_width or ny >= maze_height:
            continue
        if maze_pixels[nx, ny] == wall_color:
            maze_pixels[x + dx // 2, y + dy // 2] = channel_color
            generate_maze(nx, ny)

# 调用生成迷宫函数，起点为(maze_width//2, maze_height//2)
generate_maze(maze_width//2, maze_height//2)

# 将起点和终点设置为对应的颜色
START_X,START_Y = random.randint(1,maze_width-2), random.randint(1,maze_height-2)
while maze_pixels[START_X, START_Y]!= channel_color:
    START_X,START_Y = random.randint(1,maze_width-2), random.randint(1,maze_height-2)
    
GOAL_X, GOAL_Y = random.randint(1,maze_width-2), random.randint(1,maze_height-2)
while maze_pixels[GOAL_X, GOAL_Y]!= channel_color or ((START_X,START_Y)==(GOAL_X, GOAL_Y)):
    GOAL_X, GOAL_Y = random.randint(1,maze_width-2), random.randint(1,maze_height-2)

maze_pixels[START_X, START_Y] = start_color
maze_pixels[GOAL_X, GOAL_Y] = end_color

# 保存迷宫图像
SCALE = 5
title = 'maze05'
maze_image.save(f"{title}.png")
enlarged_image = maze_image.resize((maze_width*SCALE, maze_height*SCALE),resample=Image.Resampling.NEAREST) # 放大保存
enlarged_image.save(f"{title}_enlarged.png")
