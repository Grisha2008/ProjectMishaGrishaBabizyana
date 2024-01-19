import pygame
import pygame_gui
import Board_Create
from random import randint

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
image_normal = pygame.image.load('321-3217993_freddy-plush-fnaf-plush-pixel-art-transformed.png')  # Нормальное состояние кнопки
image_pressed = pygame.image.load('image-MANMd5Pts-transformed.png')  # Нажатое состояние кнопки

button_size = (1080, 200)
image_normal = pygame.transform.scale(image_normal, button_size)
image_pressed = pygame.transform.scale(image_pressed, button_size)

button_position = (0, window_size[1] - button_size[1])  # Позиция кнопки в левом нижнем углу
button_state = 'normal'

button_sound = pygame.mixer.Sound('ring.mp3')
button_sound.set_volume(0.2)# Звук кнопки

screen = pygame_gui.UIManager(window_size)
clock = pygame.time.Clock()

fps = 60

# Создание кнопок и слайдеров
play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 100), (300, 100)), text='Играть', manager=screen)
exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 400), (300, 100)), text='Выйти', manager=screen)
volume_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((700, 100), (350, 100)), start_value=vol, value_range=(0, 1), manager=screen)
fps_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((700, 400), (350, 100)), start_value=fps, value_range=(20, 120), manager=screen)

# Подписи к слайдерам
volume_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((500, 100), (200, 100)), text='Громкость', manager=screen)
fps_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((500, 400), (200, 100)), text='FPS', manager=screen)

running = True

static = 1

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

# Теперь объединим эту проверку с вашей функцией move_other
def move_other(x, y):
    pk = pygame.key.get_pressed()

    new_x = x  # сохраняем новые координаты в отдельных переменных
    new_y = y

    if pk[pygame.K_a]:
        new_x -= SPEED
    if pk[pygame.K_d]:
        new_x += SPEED
    if pk[pygame.K_w]:
        new_y -= SPEED
    if pk[pygame.K_s]:
        new_y += SPEED

    temp_hero = hero
    temp_hero.rect.x = new_x
    temp_hero.rect.y = new_y

    if pygame.sprite.spritecollide(temp_hero, wall_group, False, pygame.sprite.collide_mask):
        # Если есть коллизия, не обновляем координаты героя
        return x, y
    else:
        # Если коллизии нет, возвращаем новые координаты
        x, y = new_x, new_y
        return x, y

def get_distance(coords, coords1):
    return ((coords[0] - coords1[0]) ** 2 + (coords[1] - coords1[1]) ** 2) ** 0.5


# здесь определяются константы, классы и функции
FPS = 20
WIDTH = 1080
HIGHT = 720
SPEED = 12
DAMAGE = 20
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

# hero
class Hero(pygame.sprite.Sprite):
    image = get_animation(pygame.image.load(f'Mobs/Player.png'), 48, 48, 0, 0)

    def __init__(self, hero_helth_max):
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
            print(schet_attack_anim)
            self.image = self.attack_animations[static][schet_attack_anim]
        if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s]:
            self.image = self.static_animations[static][schet_anim]
        else:
            self.image = self.animations[static][schet_anim]

    def update(self):
        self.move()



# evil
evil_group = pygame.sprite.Group()
evil_list = list()

class Evil(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load('Mobs/monster_demon.png'), (100, 100))

    def __init__(self, evil_helth_max):
        super().__init__(all_sprites)
        self.add(evil_group)
        evil_list.append(self)
        self.image = Evil.image
        self.direction = "right"
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.evil_helth = evil_helth_max
        self.evil_helth_max = evil_helth_max
        self.rect.x = randint(WIDTH// 2, (WIDTH // 2) * 3)
        self.rect.y = randint(HIGHT// 2, (HIGHT // 2) * 3)
    
    def get_cords(self):
        return self.rect.x, self.rect.y

    def update(self):
        if hero.rect.y > self.rect.y - 36:
            self.rect.y += 4
        elif hero.rect.y < self.rect.y - 36:
            self.rect.y -= 4
        if hero.rect.x > self.rect.x - 32:
            self.rect.x += 4
            if self.direction != "left":
                self.image = pygame.transform.flip(self.image, True, False)
                self.direction = "left"
        elif hero.rect.x < self.rect.x - 32:
            self.rect.x -= 4
            if self.direction != "right":
                self.image = pygame.transform.flip(self.image, True, False)
                self.direction = "right"
        if self.evil_helth <= 0:
            self.kill()

        # мерием расстояние от героя до злодея
        if get_distance(hero.get_cords(), self.get_cords()) <= 100:
            hero.hero_helth -= 1

        # Hit bar злодея
        if self.evil_helth >= 0:
            pygame.draw.rect(screen_game, (255 - self.evil_helth, self.evil_helth, 0), (
            self.rect.x - 90, self.rect.y - 15, 300 - (self.evil_helth_max - self.evil_helth) * 300 // self.evil_helth_max,
            18))

        self.rect.x, self.rect.y = move_other(self.rect.x, self.rect.y)

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
        self.rect.x, self.rect.y = move_other(self.rect.x, self.rect.y)

wall_group = pygame.sprite.Group()
class wall(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load('Map/Set 1.png'), (200, 200))

    def __init__(self):
        super().__init__(all_sprites)
        self.add(floor_group)
        self.image = wall.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x, self.rect.y = move_other(self.rect.x, self.rect.y)

# Создание экземпляров floor
print(Map)
for i in range(-2, 8):
    for j in range(-3, 7):
        if Map[j + 3][i + 2] == 0:
            # Создаём экземпляр floor в каждой позиции (i, j)
            new_floor = floor()
            new_floor.rect.x = i * 200
            new_floor.rect.y = j * 200
            # Добавляем в группу спрайтов
            floor_group.add(new_floor)
        else:
            new_wall = wall()
            new_wall.rect.x = i * 200
            new_wall.rect.y = j * 200
            # Добавляем в группу спрайтов
            wall_group.add(new_wall)


class Chest(pygame.sprite.Sprite):
    pass

# border
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

play = False
# for i in range(3):
#     Evil(250)
hero = Hero(999999999999999)
schet_fps = 0
schet_anim = 0
schet_attack_anim = 0
schet_attack_fps = 1
x_pos = 0
y_pos = 0

# главный цикл
while running:
    if play:
        pk = pygame.key.get_pressed()
        clock.tick(FPS)
        # цикл обработки событи
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                play = False
            if event.type == pygame.MOUSEBUTTONDOWN and not pygame.mixer.get_busy():
                if event.button == 1:
                    shooting_sound.play()
                    hero.attack = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    play = False
                    pygame.mixer.music.load('Music.mp3')
                    pygame.mixer.music.play(-1)
                    vol = 0.1
                if event.key == pygame.K_F11:  # Переключение между полноэкранным и оконным режимами
                    fullscreen = not fullscreen
                    if fullscreen:
                        window = pygame.display.set_mode(window_size, pygame.FULLSCREEN)
                    else:
                        window = pygame.display.set_mode(window_size)
        if not pygame.mixer.get_busy():
            hero.attack = False

        if pk[pygame.K_a]:
            static = 3
        if pk[pygame.K_d]:
            static = 1
        if pk[pygame.K_w]:
            static = 2
        if pk[pygame.K_s]:
            static = 0

        # background
        screen_game.fill((255, 255, 255))

        if not True:
            text(screen, 'You Win, press "F" to exit the game')
            if pk[pygame.K_f]:
                play = False

        # Hit bar героя
        pygame.draw.rect(screen_game, (0, 200, 0),
                         (0, 0, 200 - (hero.hero_helth_max - hero.hero_helth) * 2, 25))

        # обновление экрана
        all_sprites.update()
        all_sprites.draw(screen_game)
        schet_fps += 1
        if schet_fps % 2 == 0:
            schet_anim += 1
        if hero.attack:
            schet_attack_fps += 1
        if schet_attack_fps % 3 == 0:
            schet_attack_anim += 1
        if schet_anim >= 6:
            schet_anim = 0
        if not pygame.mixer.get_busy():
            hero.attack = False
        if schet_attack_anim >= 4:
            schet_attack_anim = 0
        if not hero.attack:
            schet_attack_anim = 0
        pygame.draw.rect(screen_game, (0, 200, 0),
                         (0, 0, 200 - (hero.hero_helth_max - hero.hero_helth) * 2, 25))
        pygame.display.update()
    else:
        time_delta = clock.tick(fps) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(button_position[0], button_position[1], button_size[0], button_size[1]).collidepoint(event.pos):
                    button_state = 'pressed'
                    button_sound.play()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == exit_button:
                    running = False
                elif event.ui_element == play_button:
                    play = True
                    pygame.mixer.music.load('PlayArrow_-_Chipi-Chipi-Chapa-Chapa_77099952.mp3')
                    pygame.mixer.music.play(-1)

            if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == volume_slider:
                    vol = event.value
                    pygame.mixer.music.set_volume(vol)
                elif event.ui_element == fps_slider:
                    fps = event.value

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


