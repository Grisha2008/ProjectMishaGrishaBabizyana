import pygame
import pygame_gui
import Board_Create
from random import randint
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QListWidget, QDialog, QLineEdit
import PyQt5.QtWidgets
import sys
import numpy as np

pygame.init()
pygame.mixer.init()

window_size = (1080, 720)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Игровое меню")

# Загрузка и настройка фоновой картинки
background_image = pygame.image.load('img_2.png')  # Укажите путь к вашему изображению
background_image = pygame.transform.scale(background_image, window_size)

# Фоновая музыка
pygame.mixer.music.load('Music.mp3')
pygame.mixer.music.play(-1)

vol = 0.1
pygame.mixer.music.set_volume(vol)

# Загрузка изображений для кнопки
image_normal = pygame.image.load(
    '321-3217993_freddy-plush-fnaf-plush-pixel-art-transformed.png')  # Нормальное состояние кнопки
image_pressed = pygame.image.load('image-MANMd5Pts-transformed.png')  # Нажатое состояние кнопки

button_size = (1080, 200)
image_normal = pygame.transform.scale(image_normal, button_size)
image_pressed = pygame.transform.scale(image_pressed, button_size)

button_position = (0, window_size[1] - button_size[1])  # Позиция кнопки в левом нижнем углу
button_state = 'normal'

button_sound = pygame.mixer.Sound('ring.mp3')
button_sound.set_volume(0.2)  # Звук кнопки

screen = pygame_gui.UIManager(window_size)
clock = pygame.time.Clock()

fps = 60

# Создание кнопок и слайдеров
play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 100), (300, 100)), text='Играть',
                                           manager=screen)
exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 400), (300, 100)), text='Выйти',
                                           manager=screen)
volume_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((700, 100), (350, 100)),
                                                       start_value=vol, value_range=(0, 1), manager=screen)
# Подписи к слайдерам
volume_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((500, 100), (200, 100)), text='Громкость',
                                           manager=screen)
qt_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((700, 400), (300, 100)),
    text='Открыть PyQt',
    manager=screen
)

custom_map_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 250), (300, 100)),
    text='Custom Map',
    manager=screen
)
running = True

static = 1

# Размеры окна
width, height = 1080, 720
window = pygame.display.set_mode((width, height))

# Размеры клетки, кнопки и поля для текста
cell_size = 60  # Рассчитываем размер клетки исходя из ширины окна
button_height = 50
text_input_height = 50
matrix_height = cell_size * 9  # Высота матрицы

# Создание матрицы 9x9 с использованием NumPy
matrix = np.zeros((9, 9), dtype=int)

# Счетчик белых клеток
white_cells_count = 0

# Функция для отрисовки матрицы
def draw_matrix(win, matrix):
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            color = (255, 255, 255) if matrix[row, col] == 1 else (0, 0, 0)
            pygame.draw.rect(win, color, (col * cell_size, row * cell_size, cell_size, cell_size))
            pygame.draw.rect(win, (128, 128, 128), (col * cell_size, row * cell_size, cell_size, cell_size), 1)

# Функция для отрисовки кнопки
def draw_button(win, text, y, height):
    pygame.draw.rect(win, (200, 200, 200), (0, y, width, height))
    font = pygame.font.SysFont(None, 36)
    text_surf = font.render(text, True, (0, 0, 0))
    text_rect = text_surf.get_rect(center=(width // 2, y + height // 2))
    win.blit(text_surf, text_rect)

# Функция для сохранения матрицы
def save_matrix(matrix, map_name):
    with open('Maps.txt', 'a') as file:
        file.write(f'{map_name}: {np.array2string(matrix, separator=", ")}\n')

# Инициализация поля для ввода текста
font = pygame.font.Font(None, 36)
text = ''
input_rect = pygame.Rect(50, height - text_input_height - 100, width - 100, text_input_height)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
color = color_passive
active = False

Custom_map = False

def text(screen, text1):
    font = pygame.font.SysFont('', 60)
    text = font.render(text1, True, (255, 00, 50))
    text_x = x - 300
    text_y = y
    screen.blit(text, (text_x, text_y))


def get_animation(sheet, width, hieght, x, y):
    image = pygame.Surface((width, hieght), pygame.SRCALPHA)
    image.blit(sheet, (0, 0), (x, y, width, hieght))
    image = pygame.transform.scale(image, (144, 144))
    return image


# def move_other(x, y):
#    pk = pygame.key.get_pressed()
#
#    if pk[pygame.K_a]:
#        x += SPEED
#    elif pk[pygame.K_d]:
#        x -= SPEED
#    elif pk[pygame.K_w]:
#        y += SPEED
#    elif pk[pygame.K_s]:
#        y -= SPEED
#
#
#
#    return x, y

def get_distance(coords, coords1):
    return ((coords[0] - coords1[0]) ** 2 + (coords[1] - coords1[1]) ** 2) ** 0.5


# здесь определяются константы, классы и функции
FPS = 20
WIDTH = 1080
HIGHT = 720
SPEED = 12
DAMAGE = 100
SCORE = 0
x = WIDTH / 2
y = HIGHT / 2

# здесь происходит инициация, создание объектов и др.
screen_game = pygame.display.set_mode((WIDTH, HIGHT))
# музыка
shooting_sound = pygame.mixer.Sound('korotkiy-moschnyiy-zamah.mp3')
shooting_sound.set_volume(1)
# название приложения
pygame.display.set_caption('Лучшая игра')
# Все спрайты
all_sprites = pygame.sprite.Group()
fullscreen = False

Map = Board_Create.matrix
print(Map)

class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HIGHT // 2)


camera = Camera()

class MapsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Выбор карты")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()
        self.listWidget = QListWidget()
        self.load_maps()

        self.selectButton = QPushButton("Выбрать карту")
        self.selectButton.clicked.connect(self.select_map)
        self.deleteButton = QPushButton("Удалить карту")
        self.deleteButton.clicked.connect(self.delete_map)

        layout.addWidget(self.listWidget)
        layout.addWidget(self.selectButton)
        layout.addWidget(self.deleteButton)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def load_maps(self):
        with open('Maps.txt', 'r') as file:
            self.listWidget.clear()
            for line in file:
                self.listWidget.addItem(line.strip())

    def select_map(self):
        global matrix, play, running # Обращаемся к глобальной переменной
        selected_map = self.listWidget.currentItem().text()
        map_name, map_data = selected_map.split(': ')
        print("Выбрана карта:", map_name)
        # Преобразование строки данных матрицы обратно в массив NumPy
        matrix = np.fromstring(map_data.replace('[', '').replace(']', ''), sep=', ', dtype=int).reshape(9, 9)
        if matrix:
            play = True
        else:
            running = False
 

    def delete_map(self):
        # Здесь код для удаления карты
        currentRow = self.listWidget.currentRow()
        if currentRow >= 0:
            self.listWidget.takeItem(currentRow)

def open_maps_window():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    Mapswindow = MapsWindow()
    Mapswindow.show()
    sys.exit(app.exec_())
# Запуск PyQt приложения

class SaveMapDialog(QDialog):
    def __init__(self, matrix, parent=None):
        super().__init__(parent)
        self.matrix = matrix
        self.setWindowTitle("Сохранение карты")

        self.layout = QVBoxLayout(self)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Введите название карты")
        self.layout.addWidget(self.name_input)

        self.save_button = QPushButton("Сохранить", self)
        self.save_button.clicked.connect(self.save_map)
        self.layout.addWidget(self.save_button)

    def save_map(self):
        map_name = self.name_input.text()
        save_matrix(self.matrix, map_name)
        self.close()


def save_matrix(matrix, map_name):
    with open('Maps.txt', 'a') as file:
        matrix_change = []
        for i in range(len(matrix)):
            matrix_change.append([])
            for k in matrix[i]:
                matrix_change[i].append(k)
        matrix = matrix_change
        print(matrix)
        file.write(f'{map_name}: {str(matrix)}\n')


# Функция для открытия диалога сохранения карты
def open_save_dialog(matrix):
    app = QApplication(sys.argv)
    dialog = SaveMapDialog(matrix)
    dialog.exec_()
# hero
class Hero(pygame.sprite.Sprite):
    image = get_animation(pygame.image.load(f'Mobs/Player.png'), 48, 48, 0, 0)

    def __init__(self, hero_helth_max, walls):
        super().__init__(all_sprites)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.hero_helth = hero_helth_max
        self.hero_helth_max = hero_helth_max
        self.rect.x = x - 100
        self.rect.y = y - 100
        self.animations = []
        self.attack = 0
        self.walls = walls
        self.dx = 0
        self.dy = 0
        self.attack_animations = []
        self.static_animations = []
        for i in range(3):
            self.static_animations.append(
                [get_animation(pygame.image.load(f'Mobs/Player.png'), 48, 48, j * 48, i * 48) for j in range(6)])
        self.static_animations.append(
            [get_animation(pygame.image.load(f'Mobs/Player.png'), 48, 48, j * 48, 48) for j in range(1)])
        self.static_animations[3] = self.static_animations[1].copy()
        for i in range(len(self.static_animations[3])):
            self.static_animations[3][i] = pygame.transform.flip(self.static_animations[3][i], True, False)
        for i in range(3, 7):
            self.animations.append(
                [get_animation(pygame.image.load(f'Mobs/Player.png'), 48, 48, j * 48, i * 48) for j in range(6)])
        self.animations.append(
            [get_animation(pygame.image.load(f'Mobs/Player.png'), 48, 48, j * 48, 48) for j in range(1)])
        self.animations[3] = self.animations[1].copy()
        for i in range(len(self.animations[3])):
            self.animations[3][i] = pygame.transform.flip(self.animations[3][i], True, False)
        for i in range(7, 9):
            self.attack_animations.append(
                [get_animation(pygame.image.load(f'Mobs/Player.png'), 48, 48, j * 48, i * 48) for j in range(4)])
        self.attack_animations.append([])
        for i in range(len(self.attack_animations[0])):
            self.attack_animations[-1].append(pygame.transform.flip(self.attack_animations[0][i], True, False))
        self.attack_animations.append(
            [get_animation(pygame.image.load(f'Mobs/Player.png'), 48, 48, j * 48, 6 * 48) for j in range(4)])

    def get_cords(self):
        return self.rect.x, self.rect.y

    def move(self):
        keys = pygame.key.get_pressed()
        if self.attack:
            self.image = self.attack_animations[(static_anim - 1) % 4][attack_anim]
        elif not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s]:
            self.image = self.static_animations[static][schet_anim]
        else:
            self.image = self.animations[static][schet_anim]

    def movement(self, dx=0, dy=0):
        if dx != 0:
            self.rect.x += dx
            if pygame.sprite.spritecollide(self, self.walls, False):
                if dx > 0:
                    self.rect.right = min(
                        wall.rect.left for wall in pygame.sprite.spritecollide(self, self.walls, False))
                elif dx < 0:
                    self.rect.left = max(
                        wall.rect.right for wall in pygame.sprite.spritecollide(self, self.walls, False))

        if dy != 0:
            self.rect.y += dy
            if pygame.sprite.spritecollide(self, self.walls, False):
                if dy > 0:
                    self.rect.bottom = min(
                        wall.rect.top for wall in pygame.sprite.spritecollide(self, self.walls, False))
                elif dy < 0:
                    self.rect.top = max(
                        wall.rect.bottom for wall in pygame.sprite.spritecollide(self, self.walls, False))

    def update(self):
        self.dx, self.dy = 0, 0
        if pk[pygame.K_a]:
            self.dx -= SPEED
        if pk[pygame.K_d]:
            self.dx += SPEED
        if pk[pygame.K_w]:
            self.dy -= SPEED
        if pk[pygame.K_s]:
            self.dy += SPEED

        self.movement(self.dx, self.dy)
        self.move()


# evil
evil_group = pygame.sprite.Group()
evil_list = list()


class Evil(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load('Mobs/monster_demon.png'), (100, 100))

    def __init__(self, evil_helth_max, walls):
        super().__init__(all_sprites)
        self.add(evil_group)
        evil_list.append(self)
        self.image = Evil.image
        self.direction = "right"
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.evil_helth =  evil_helth_max
        self.evil_helth_max = evil_helth_max
        self.walls = wall_group1
        self.dx = 0
        self.dy = 0

        self.rect.x = 200
        self.rect.y = 200 
        self.walls = wall_group1
        self.dx = 0
        self.dy = 0

    def get_cords(self):
        return self.rect.x, self.rect.y

    def movement(self, dx=0, dy=0):
        if dx != 0:
            self.rect.x += dx
            if pygame.sprite.spritecollide(self, self.walls, False):
                if dx > 0:
                    self.rect.right = min(
                        wall.rect.left for wall in pygame.sprite.spritecollide(self, self.walls, False))
                elif dx < 0:
                    self.rect.left = max(
                        wall.rect.right for wall in pygame.sprite.spritecollide(self, self.walls, False))

        if dy != 0:
            self.rect.y += dy
            if pygame.sprite.spritecollide(self, self.walls, False):
                if dy > 0:
                    self.rect.bottom = min(
                        wall.rect.top for wall in pygame.sprite.spritecollide(self, self.walls, False))
                elif dy < 0:
                    self.rect.top = max(
                        wall.rect.bottom for wall in pygame.sprite.spritecollide(self, self.walls, False))

    def update(self):
        global SCORE
        # Перемещение с учетом столкновений
        self.movement(self.dx, self.dy)
        self.dx, self.dy = 0, 0
        if hero.rect.y > self.rect.y - 36:
            self.dy += 2
        elif hero.rect.y < self.rect.y - 36:
            self.dy -= 2
        if hero.rect.x > self.rect.x - 32:
            self.dx += 2
            if self.direction != "left":
                self.image = pygame.transform.flip(self.image, True, False)
                self.direction = "left"
        elif hero.rect.x < self.rect.x - 32:
            self.dx -= 2
            if self.direction != "right":
                self.image = pygame.transform.flip(self.image, True, False)
                self.direction = "right"

        self.movement(self.dx, self.dy)

        if self.evil_helth <= 0:
            SCORE += 1
            self.kill()

        # мерием расстояние от героя до злодея
        if get_distance(hero.get_cords(), self.get_cords()) <= 100 and not hero.attack:
            hero.hero_helth -= 1

        if pygame.sprite.spritecollide(self, bullet_group, True, pygame.sprite.collide_mask):
            self.evil_helth -= DAMAGE

        if get_distance(hero.get_cords(), self.get_cords()) <= 150 and hero.attack and attack_check <= 1:
            self.evil_helth -= DAMAGE

        # Hit bar злодея
        if self.evil_helth >= 0:
            pygame.draw.rect(screen_game, (255 - self.evil_helth, self.evil_helth, 0), (
                self.rect.x - 90, self.rect.y - 15,
                300 - (self.evil_helth_max - self.evil_helth) * 300 // self.evil_helth_max,
                18))


# bullet
bullet_group = pygame.sprite.Group()

class Bullet(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load('img_4.png'), (60, 60))

    def __init__(self, screen, start_x, start_y, direction_x, direction_y):
        super().__init__(all_sprites)
        self.add(bullet_group)
        self.image = Bullet.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.rect.x = start_x
        self.rect.y = start_y
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.speed = 20
        self.start_pos = start_x, start_y

    def update(self):
        self.rect.x += self.direction_x * self.speed
        self.rect.y += self.direction_y * self.speed

        if pygame.sprite.spritecollide(self, wall_group1, False, pygame.sprite.collide_mask):
            self.kill()

floor_group = pygame.sprite.Group()


class floor(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load('Map/Set 1.2.png'), (200, 200))

    def __init__(self):
        super().__init__(all_sprites)
        self.add(floor_group)
        self.image = floor.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


wall_group = pygame.sprite.Group()


class wall(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load('Map/Set 1.png'), (100, 100))

    def __init__(self):
        super().__init__(all_sprites)
        self.add(wall_group)
        self.image = wall.image
        self.rect = pygame.Rect(0, 0, 100, 80)
        self.rect = pygame.Rect(0,0,100,80)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # pygame.draw.rect(screen_game, (255,255,255), self.rect)
        pass

wall_group1 = pygame.sprite.Group()
class wall1(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load('Map/Set 1.png'), (200, 200))

    def __init__(self):
        super().__init__(all_sprites)
        self.add(wall_group1)
        self.image = wall1.image
        self.rect = self.image.get_rect()
        #self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        # pygame.draw.rect(screen_game, (255,255,255), self.rect)
        pass


wall_group1 = pygame.sprite.Group()


class wall1(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load('Map/Set 1.png'), (200, 200))

    def __init__(self):
        super().__init__(all_sprites)
        self.add(wall_group1)
        self.image = wall1.image
        self.rect = self.image.get_rect()
        # self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        # pygame.draw.rect(screen_game, (255,255,255), self.rect)
        pass

wall_group2 = pygame.sprite.Group()

# Создание экземпляров floor
for i in range(-4, 6):
    for j in range(-5, 5):
        if Map[i + 4][j + 5] == 0:
            # Создаём экземпляр floor в каждой позиции (i, j)
            new_floor = floor()
            new_floor.rect.x = i * 200
            new_floor.rect.y = j * 200
            # Добавляем в группу спрайтов
            floor_group.add(new_floor)
        else:
            new_wall = wall()
            new_wall.rect.x = i * 200 + 50
            new_wall.rect.y = j * 200 + 15
            # Добавляем в группу спрайтов

            new_wall1 = wall1()
            new_wall1.rect.x = i * 200
            new_wall1.rect.y = j * 200
            new_wall1.rect.x = i * 200
            new_wall1.rect.y = j * 200
            # Добавляем в группу спрайтов
            wall_group1.add(new_wall1)


class Chest(pygame.sprite.Sprite):
    pass


# border
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

play = False
for i in range(3):
    Evil(250, wall_group)
hero = Hero(100, wall_group)
schet_fps = 0
schet_anim = 0
attack_anim = 0
attack_fps = 1
schet_fps_bullet = 0
attack_check = 0
x_pos = 0
y_pos = 0

# главный цикл
while running:
    bullets = []
    if play:
        pk = pygame.key.get_pressed()
        clock.tick(FPS)
        # цикл обработки событи
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                play = False
            if event.type == pygame.MOUSEBUTTONDOWN and not pygame.mixer.get_busy():
                if event.button == 3 and schet_fps_bullet >= 100:
                    mouse_pos = pygame.mouse.get_pos()
                    center_x, center_y = hero.rect.center
                    direction_x, direction_y = mouse_pos[0] - center_x, mouse_pos[1] - center_y
                    distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
                    direction_x /= distance
                    direction_y /= distance
                    schet_fps_bullet -= 100
                    Bullet(screen_game, center_x - 25, center_y, direction_x, direction_y)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    play = False
                    pygame.mixer.music.load('Music.mp3')
                    pygame.mixer.music.play(-1)
                    vol = 0.1
                if event.key == pygame.K_SPACE and not hero.attack:
                    shooting_sound.play()
                    hero.attack = True
                    attack_check = 0
                    static_anim = static
                if event.key == pygame.K_F11:  # Переключение между полноэкранным и оконным режимами
                    fullscreen = not fullscreen
                    if fullscreen:
                        window = pygame.display.set_mode(window_size, pygame.FULLSCREEN)
                    else:
                        window = pygame.display.set_mode(window_size)

        if hero.attack:
            attack_check += 1
            if attack_fps < 15:
                attack_fps += 1
                if attack_fps % 5 == 0:
                    attack_anim += 1
                print(attack_anim)
            else:
                hero.attack = False
        else:
            attack_anim = 0
            attack_fps = 1



        if hero.hero_helth <= 0:
            best_score = open('best_score.txt')
            if int(best_score.read()) < SCORE:
                best_score.close()
                best_score = open('best_score.txt', 'w')
                best_score.write(str(SCORE))
                best_score.close()
            running = False

        if len(evil_group) == 0:
            for i in range(3):
                Evil(250, wall_group)


        if pk[pygame.K_a]:
            static = 3
        elif pk[pygame.K_d]:
            static = 1
        elif pk[pygame.K_w]:
            static = 2
        elif pk[pygame.K_s]:
            static = 0


        # background
        screen_game.fill((255, 255, 255))

        # Hit bar героя
        pygame.draw.rect(screen_game, (0, 200, 0),
                         (0, 0, 200 - (hero.hero_helth_max - hero.hero_helth) * 2, 25))

        # обновление экрана
        camera.update(hero)
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.draw(screen_game)
        screen_game.blit(pygame.font.Font(None, 36).render(f'score: {SCORE}', True, (180, 0, 0)), (10, 50))
        all_sprites.update()

        schet_fps += 1
        if schet_fps % 2 == 0:
            schet_anim += 1
        if schet_anim >= 6:
            schet_anim = 0
        if not pygame.mixer.get_busy():
            hero.attack = False

        if schet_fps_bullet <= 300:
            schet_fps_bullet += 3
        pygame.draw.rect(screen_game, (200, 0, 0),
                         (0, 25, schet_fps_bullet, 25))
        pygame.draw.rect(screen_game, (0, 200, 0),
                         (0, 0, 200 - (hero.hero_helth_max - hero.hero_helth) * 2, 25))
        pygame.display.update()
    elif Custom_map == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if input_rect.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_passive
                try:
                    if y < matrix_height and x < matrix_height:  # Проверка, что клик был в пределах матрицы
                        print(y)
                        col, row = x // cell_size, y // cell_size
                        if (row, col) != (4, 4):  # Исключаем центральную клетку
                            if matrix[row, col] == 0 and white_cells_count < 25:
                                matrix[row, col] = 1
                                white_cells_count += 1
                            elif matrix[row, col] == 1:
                                matrix[row, col] = 0
                                white_cells_count -= 1
                    elif y >= height - button_height - 10:  # Клик по кнопке "Сохранить"
                        open_save_dialog(matrix)
                        Custom_map = False
                except Exception:
                    pass
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        window.fill((0, 0, 0))
        draw_matrix(window, matrix)
        draw_button(window, "Сохранить", height - button_height - 10, button_height)

        pygame.display.flip()
    else:
        time_delta = clock.tick(fps) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(button_position[0], button_position[1], button_size[0], button_size[1]).collidepoint(
                        event.pos):
                    button_state = 'pressed'
                    button_sound.play()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == exit_button:
                    running = False
                elif event.ui_element == play_button:
                    play = True
                    pygame.mixer.music.load('PlayArrow_-_Chipi-Chipi-Chapa-Chapa_77099952.mp3')
                    pygame.mixer.music.play(-1)
                elif event.ui_element == custom_map_button:
                    Custom_map = True
                elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == qt_button:
                        open_maps_window()

            if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == volume_slider:
                    vol = event.value
                    pygame.mixer.music.set_volume(vol)

            screen.process_events(event)

        window.blit(background_image, (0, 0))
        if button_state == 'pressed' and not pygame.mixer.get_busy():
            button_state = 'normal'

        if button_state == 'normal':
            window.blit(image_normal, button_position)
        else:
            window.blit(image_pressed, button_position)
        # Сброс состояния кнопки

        screen.update(time_delta)
        screen.draw_ui(window)
        pygame.display.update()

