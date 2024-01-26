import numpy as np
import random

# Определение параметров матрицы и направлений для BFS
matrix = np.zeros((10, 10), dtype=int)
center_coords = [(4, 4), (4, 5), (5, 4), (5, 5)] # Центральные клетки
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
num_ones = random.randint(10, 20)

# Функция для проверки пути до центра
def is_path_to_center(matrix, center_coords):
    visited = set()
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 0 and (i, j) not in visited:
                queue = [(i, j)]
                path_to_center = False
                while queue:
                    x, y = queue.pop(0)
                    if (x, y) in center_coords:
                        path_to_center = True
                        break
                    visited.add((x, y))
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 10 and 0 <= ny < 10 and matrix[nx][ny] == 0 and (nx, ny) not in visited:
                            queue.append((nx, ny))
                if not path_to_center:
                    return False
    return True

# Генерация матрицы с исключением центральных клеток
valid_matrix = False
while not valid_matrix:
    matrix = np.zeros((10, 10), dtype=int)
    ones_placed = 0
    while ones_placed < num_ones:
        x, y = random.randint(0, 9), random.randint(0, 9)
        if matrix[x][y] == 0 and (x, y) not in center_coords:
            matrix[x][y] = 1
            ones_placed += 1
    valid_matrix = is_path_to_center(matrix, center_coords)
matr = matrix
matrix = []
for i in range(12):
    if i == 0:
        matrix.append([1] * 12)
    elif i == 11:
        matrix.append([1] * 12)
    else:
        matrix.append([])
        matrix[i].append(1)
        for k in matr[i - 1]:
            matrix[i].append(k)
        matrix[i].append(1)

