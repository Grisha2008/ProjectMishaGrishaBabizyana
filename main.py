import pygame
import pygame_gui
import Board_Create

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


def text(screen, text1):
    font = pygame.font.SysFont('', 60)
    text = font.render(text1, True, (255, 00, 50))
    text_x = x - 300
    text_y = y
    screen.blit(text, (text_x, text_y))


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
shooting_sound = pygame.mixer.Sound('data/shoot.wav')
shooting_sound.set_volume(0.1)
# название приложения
pygame.display.set_caption('Лучшая игра')
# Все спрайты
all_sprites = pygame.sprite.Group()


# hero
class Hero(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load('Player/Стоит смотрит/Слой 2.png'), (80, 80))

    def __init__(self, hero_helth_max):
        super().__init__(all_sprites)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.hero_helth = hero_helth_max
        self.hero_helth_max = hero_helth_max
        self.rect.x = x - 80
        self.rect.y = y
        self.static = 0

    def update(self):
        pk = pygame.key.get_pressed()
        if pk[pygame.K_d]:
            if schet_anim == 0:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вбок/Слой 26.png'),(80, 80))
            elif schet_anim == 1:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вбок/Слой 27.png'),(80, 80))
            elif schet_anim == 2:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вбок/Слой 28.png'),(80, 80))
            elif schet_anim == 3:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вбок/Слой 29.png'),(80, 80))
            elif schet_anim == 4:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вбок/Слой 30.png'),(80, 80))
            elif schet_anim == 5:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вбок/Слой 31.png'),(80, 80))
            self.static = 3
        if pk[pygame.K_a]:
            if schet_anim == 0:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вбок/Слой 26.png'),(80, 80))
            elif schet_anim == 1:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вбок/Слой 27.png'),(80, 80))
            elif schet_anim == 2:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вбок/Слой 28.png'),(80, 80))
            elif schet_anim == 3:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вбок/Слой 29.png'),(80, 80))
            elif schet_anim == 4:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вбок/Слой 30.png'),(80, 80))
            elif schet_anim == 5:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вбок/Слой 31.png'),(80, 80))
            self.image = pygame.transform.flip(self.image, True, False)
            self.static = 2
        if pk[pygame.K_w]:
            if schet_anim == 0:
                self.image = pygame.transform.scale(pygame.image.load('Player/Уходит((/Слой 32.png'),(80, 80))
            elif schet_anim == 1:
                self.image = pygame.transform.scale(pygame.image.load('Player/Уходит((/Слой 33.png'),(80, 80))
            elif schet_anim == 2:
                self.image = pygame.transform.scale(pygame.image.load('Player/Уходит((/Слой 34.png'),(80, 80))
            elif schet_anim == 3:
                self.image = pygame.transform.scale(pygame.image.load('Player/Уходит((/Слой 35.png'),(80, 80))
            elif schet_anim == 4:
                self.image = pygame.transform.scale(pygame.image.load('Player/Уходит((/Слой 36.png'),(80, 80))
            elif schet_anim == 5:
                self.image = pygame.transform.scale(pygame.image.load('Player/Уходит((/Слой 37.png'),(80, 80))
            self.static = 1
        if pk[pygame.K_s]:
            if schet_anim == 0:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вперед/Слой 20.png'),(80, 80))
            elif schet_anim == 1:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вперед/Слой 21.png'),(80, 80))
            elif schet_anim == 2:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вперед/Слой 22.png'),(80, 80))
            elif schet_anim == 3:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вперед/Слой 23.png'),(80, 80))
            elif schet_anim == 4:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вперед/Слой 24.png'),(80, 80))
            elif schet_anim == 5:
                self.image = pygame.transform.scale(pygame.image.load('Player/Идет вперед/Слой 25.png'),(80, 80))
            self.static = 0
        if not pk[pygame.K_s] and not pk[pygame.K_w] and not pk[pygame.K_a] and not pk[pygame.K_d]:
             if self.static == 0:
                 if schet_anim == 0:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Стоит смотрит/Слой 2.png'), (80, 80))
                 elif schet_anim == 1:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Стоит смотрит/Слой 3.png'), (80, 80))
                 elif schet_anim == 2:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Стоит смотрит/Слой 4.png'), (80, 80))
                 elif schet_anim == 3:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Стоит смотрит/Слой 5.png'), (80, 80))
                 elif schet_anim == 4:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Стоит смотрит/Слой 6.png'), (80, 80))
                 elif schet_anim == 5:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Стоит смотрит/Слой 7.png'), (80, 80))
             if self.static == 1:
                 if schet_anim == 0:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Отвернулся Гадина/Слой 14.png'), (80, 80))
                 elif schet_anim == 1:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Отвернулся Гадина/Слой 15.png'), (80, 80))
                 elif schet_anim == 2:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Отвернулся Гадина/Слой 16.png'), (80, 80))
                 elif schet_anim == 3:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Отвернулся Гадина/Слой 17.png'), (80, 80))
                 elif schet_anim == 4:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Отвернулся Гадина/Слой 18.png'), (80, 80))
                 elif schet_anim == 5:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Отвернулся Гадина/Слой 19.png'), (80, 80))
             if self.static == 2:
                 if schet_anim == 0:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Смотрит вбок/Слой 8.png'), (80, 80))
                 elif schet_anim == 1:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Смотрит вбок/Слой 9.png'), (80, 80))
                 elif schet_anim == 2:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Смотрит вбок/Слой 10.png'), (80, 80))
                 elif schet_anim == 3:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Смотрит вбок/Слой 11.png'), (80, 80))
                 elif schet_anim == 4:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Смотрит вбок/Слой 12.png'), (80, 80))
                 elif schet_anim == 5:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Смотрит вбок/Слой 13.png'), (80, 80))
                 self.image = pygame.transform.flip(self.image, True, False)
             if self.static == 3:
                 if schet_anim == 0:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Смотрит вбок/Слой 8.png'), (80, 80))
                 elif schet_anim == 1:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Смотрит вбок/Слой 9.png'), (80, 80))
                 elif schet_anim == 2:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Смотрит вбок/Слой 10.png'), (80, 80))
                 elif schet_anim == 3:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Смотрит вбок/Слой 11.png'), (80, 80))
                 elif schet_anim == 4:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Смотрит вбок/Слой 12.png'), (80, 80))
                 elif schet_anim == 5:
                     self.image = pygame.transform.scale(pygame.image.load('Player/Смотрит вбок/Слой 13.png'), (80, 80))


# evil
evil_group = pygame.sprite.Group()


class Evil(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load('Мобы/monster_demon.png'), (100, 100))

    def __init__(self, evil_helth_max):
        super().__init__(all_sprites)
        self.add(evil_group)
        self.image = Evil.image
        self.direction = "right"
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.evil_helth = evil_helth_max
        self.evil_helth_max = evil_helth_max
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pk = pygame.key.get_pressed()
        if hero.rect.y > self.rect.y:
            self.rect.y += 4
        elif hero.rect.y < self.rect.y:
            self.rect.y -= 4
        if hero.rect.x > self.rect.x:
            self.rect.x += 4
            if self.direction != "left":
                self.image = pygame.transform.flip(self.image, True, False)
                self.direction = "left"
        elif hero.rect.x < self.rect.x:
            self.rect.x -= 4
            if self.direction != "right":
                self.image = pygame.transform.flip(self.image, True, False)
                self.direction = "right"
        if self.evil_helth <= 0:
            self.kill()
        if pk[pygame.K_a]:
            self.rect.x += SPEED
        if pk[pygame.K_d]:
            self.rect.x -= SPEED
        if pk[pygame.K_w]:
            self.rect.y += SPEED
        if pk[pygame.K_s]:
            self.rect.y -= SPEED


class Chest(pygame.sprite.Sprite):
    pass
# bullet
bullet_group = pygame.sprite.Group()

class Bullet(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load('data/hero.png'), (10, 10))

    def __init__(self, pos, finpos):
        super().__init__(all_sprites)
        self.add(bullet_group)
        self.image = Bullet.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.finpos = finpos
        self.kx = self.finpos[0] - self.rect.x
        self.ky = self.finpos[1] - self.rect.y

    def update(self):
        pk = pygame.key.get_pressed()
        kx = self.kx
        ky = self.ky
        try:
            if kx * ky != 0:
                self.rect = self.rect.move(int((5 * kx / abs(kx)) * abs(kx / ky)),
                                           int((5 * ky / abs(ky)) * abs(ky / kx)))
        except:
            pass
        if pk[pygame.K_a]:
            self.rect.x += SPEED
        if pk[pygame.K_d]:
            self.rect.x -= SPEED
        if pk[pygame.K_w]:
            self.rect.y += SPEED
        if pk[pygame.K_s]:
            self.rect.y -= SPEED
        if pygame.sprite.spritecollideany(self, evil_group):
            evil.evil_helth -= DAMAGE
            self.kill()



# border
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


Border(5, 5, WIDTH - 5, 5)
Border(5, HIGHT - 5, WIDTH - 5, HIGHT - 5)
Border(5, 5, 5, HIGHT - 5)
Border(WIDTH - 5, 5, WIDTH - 5, HIGHT - 5)
play = False
evil = Evil(250)
hero = Hero(100)
schet_fps = 0
schet_anim = 0

# главный цикл
while running:
    if play:
        clock.tick(FPS)
        # цикл обработки событи
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                play = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                shooting_sound.play()
                Bullet((hero.rect.x, hero.rect.y), event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    play = False
                    pygame.mixer.music.load('Music.mp3')
                    pygame.mixer.music.play(-1)
                    vol = 0.1
        # background
        screen_game.fill((255, 255, 255))
        if not True:
            text(screen, 'You Win, press "F" to exit the game')
            if pk[pygame.K_f]:
                play = False
        # Hit bar героя
        pygame.draw.rect(screen_game, (0, 200, 0),
                         (hero.rect.x - 55, hero.rect.y - 35, 200 - (hero.hero_helth_max - hero.hero_helth) * 2, 25))
        # Hit bar злодея
        if evil.evil_helth >= 0:
            pygame.draw.rect(screen_game, (255 - evil.evil_helth, evil.evil_helth, 0), (
            evil.rect.x - 90, evil.rect.y - 15, 300 - (evil.evil_helth_max - evil.evil_helth) * 300 // evil.evil_helth_max,
            18))

        # обновление экрана
        all_sprites.update()
        all_sprites.draw(screen_game)
        schet_fps += 1
        if schet_fps >= 2:
            schet_anim += 1
            schet_fps = 0
        if schet_anim >= 6:
            schet_anim = 0
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
                    pygame.mixer.music.load('data/zxc.mp3')
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


