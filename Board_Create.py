import random
import pygame

TestBoard = [[2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

class Board:
    def __init__(self, Board):
        self.size = 10
        self.board = Board
        self.left = 10
        self.top = 10
        self.cell_size = 100


    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def is_path_available(self, start, end):
        # Поиск в ширину для проверки пути
        queue = [start]
        visited = set()
        while queue:
            x, y = queue.pop(0)
            if (x, y) == end:
                return True
            visited.add((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Соседние клетки
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size and (nx, ny) not in visited and self.board[ny][nx] == 0:
                    queue.append((nx, ny))
        return False

    def render(self):
        while sum(row.count(1) for row in self.board) < random.randint(20, 81):
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if (x, y) != (0, 0) and (x, y) != (9, 9):  # Исключаем левый верхний угол
                original_value = self.board[y][x]
                self.board[y][x] = 1
                if not self.is_path_available((0, 0), (self.size - 1, self.size - 1)):
                    self.board[y][x] = original_value  # Восстанавливаем, если путь блокирован
        return self.board

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if 0 <= cell_x < self.size and 0 <= cell_y < self.size:
            return cell_x, cell_y
        return None

    def on_click(self, cell_coords):
        if cell_coords:
            print("Click on cell:", cell_coords)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
