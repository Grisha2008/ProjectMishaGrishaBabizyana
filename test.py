import pygame
import math

# Инициализация Pygame
pygame.init()

# Устанавливаем размеры окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Выстрел из центра")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Количество кадров в секунду
clock = pygame.time.Clock()

class Bullet:
    def __init__(self, screen, start_x, start_y, direction_x, direction_y):
        self.screen = screen
        self.x = start_x
        self.y = start_y
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.speed = 5

    def update(self):
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed
        self.draw()

    def draw(self):
        pygame.draw.circle(self.screen, RED, (int(self.x), int(self.y)), 10)

def main():
    running = True
    bullets = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Правая кнопка мыши
                mouse_pos = pygame.mouse.get_pos()
                center_x, center_y = width // 2, height // 2
                direction_x, direction_y = mouse_pos[0] - center_x, mouse_pos[1] - center_y
                distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
                direction_x /= distance
                direction_y /= distance
                bullets.append(Bullet(screen, center_x, center_y, direction_x, direction_y))

        screen.fill(WHITE)

        for bullet in bullets:
            bullet.update()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()