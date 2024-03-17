def generate_pascal_triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = generate_pascal_triangle(n - 1)
        last_row = triangle[-1]
        new_row = [1] + [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)] + [1]
        triangle.append(new_row)
        return triangle

def flatten_triangle(triangle):
    flattened = [num for row in triangle for num in row]
    return flattened

rows = 5  # 设置要生成的行数
triangle = generate_pascal_triangle(rows)
result = flatten_triangle(triangle)
print(result)
