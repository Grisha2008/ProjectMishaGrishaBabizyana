import numpy as np
import random

# Define the matrix dimensions
matrix = np.zeros((10, 10), dtype=int)
center_coords = [(4, 4), (4, 5), (5, 4), (5, 5)]  # Center coordinates for 10x10 matrix
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
num_ones = random.randint(10, 20)  # Number of ones to place in addition to the border

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

# Function to fill the edges with 1s
def fill_edges(matrix):
    matrix[0, :] = 1
    matrix[-1, :] = 1
    matrix[:, 0] = 1
    matrix[:, -1] = 1

valid_matrix = False
while not valid_matrix:
    matrix = np.zeros((10, 10), dtype=int)
    fill_edges(matrix)  # Fill edges with 1s
    ones_placed = 0
    while ones_placed < num_ones:
        x, y = random.randint(1, 8), random.randint(1, 8)  # Avoid edges
        if matrix[x][y] == 0 and (x, y) not in center_coords:
            matrix[x][y] = 1
            ones_placed += 1
    valid_matrix = is_path_to_center(matrix, center_coords)
print(matrix)