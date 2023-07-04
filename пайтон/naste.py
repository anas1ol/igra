import pygame
import random
import math
import time
pygame.init()
#импортировали все используемые библиотеки

DESERT = pygame.image.load("imgs/desert.jpg")
FINISH = pygame.image.load("imgs/finish.png")
CAR = pygame.image.load("imgs/track.png")#грузовик как у новой почты, просто рисую плохо
CAR = pygame.transform.rotate(CAR, 90)
WALL =pygame.image.load("imgs/wall.png")
WIDTH, HEIGHT = DESERT.get_width()/1.2, DESERT.get_height()#задали ширину и высоту игрового окна
LINE = pygame.transform.rotate(FINISH, 90)
FINISH_LINE = pygame.transform.scale(LINE, (50, HEIGHT))
#задали все нужные картинки
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game for Taras Pavlov")
font = pygame.font.Font(None, 72)
text1 = font.render("You LOSE!", True, (0, 0, 0))
text2 = font.render("You WIN!", True, (255, 255, 255))
#прописали все надписи
FPS = 60#количество кадров в сек
run = True
coord = []
for i in range(15):
    coord.append(random.randint(150, int(WIDTH-150)))
    coord.append(random.randint(100, int(HEIGHT-100)))
#задали рандомные координаты для препятствий где 2n елемент это всегда х,а 2n+1 вегда у
x=0.1 *0.1*0.1*0.9*0.86*1.2/15*1.1/15*1/15*0.9/15*0.8/15*0.7/15*0.6/15*0.5/15*0.4/15*0.3/15
print(x)
# вероятность что препятсвия встанят в один ряд и закроют проезд к финишу))

class Car:
    def __init__(self):
        self.img = self.IMG
        self.max_speed = 5
        self.speed = 0
        self.rotation_speed = 4
        self.incline = 270
        self.x, self.y = self.START_POS
        self.acceleration = 0.08
    #инициализируем и задаём параметры для нашей машинки
def rotate(self, left=False, right=False):
        if left:
            self.incline += self.rotation_speed
        elif right:
            self.incline -= self.rotation_speed
    #функция которая обновляет градус поворота при нажатой кнопке поворота

def draw(self, screen):
        screen.blit(FINISH_LINE, (WIDTH - 50, 0))
        #отрисовуем финишную черту

        n = 0
        while n <= 29:
            screen.blit(WALL, (coord[n],coord[n+1]))
            n +=2
        #отрисовуем 15 препятсвий используя список координат который мы создали ранее

        rotated_image = pygame.transform.rotate(self.img, self.incline)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        screen.blit(rotated_image, new_rect.topleft)
        #поворачиваем и отрисовуем машинку на актуальный угол

def move_manager(self, moved_up):
        self.speed = min(self.speed + self.acceleration, self.max_speed)
        if moved_up:
            self.move()
        else:
            self.back_move()
    #функция которая по приходящему аргументу понимает в какую сторону происходит движение и вызывает нужную
    #функцию для обновления текущей позиции машинки

def move(self):
        radians = math.radians(self.incline)
        vertical = math.cos(radians) * self.speed
        horizontal = math.sin(radians) * self.speed

        self.y -= vertical
        self.x -= horizontal
        #обновление координат машинки когда она едет вперёд

        if self.x<=0:
            self.x =0
        if self.x>=WIDTH:
            self.x =WIDTH
        if self.y<=0:
            self.y =0
        if self.y>=HEIGHT-70:
            self.y =HEIGHT-70
        #ограничение для машинки что бы она не выезжала за края игрового поля когда она едет передом

def back_move(self):
        radians = math.radians(self.incline)
        vertical = math.cos(radians) * self.speed/2
        horizontal = math.sin(radians) * self.speed/2

        self.y += vertical
        self.x += horizontal
        #обновление координат машинки когда она едет назад
        if self.x <= 0:
            self.x = 0
        if self.x >= WIDTH:
            self.x = WIDTH
        if self.y <= 0:
            self.y = 0
        if self.y >= HEIGHT - 70:
            self.y = HEIGHT -70
        #ограничение для машинки что бы она не выезжала за края игрового поля когда она едет задом
        def acceleration_speed(self):
         self.speed = max(self.speed - self.acceleration, 0)
        self.move()
    #функция которая обновляет моментальную скорость когда машинка не ускоряеться и вызывает функцию которая обновляет
    #позицию машинки

def acceleration_speed_back(self):
        self.speed = max(self.speed - self.acceleration, 0)
        self.back_move()
    # функция которая обновляет моментальную скорость когда машинка не ускоряеться и вызывает функцию которая обновляет
    # позицию машинки

class PCar(Car):
    IMG = CAR
    START_POS = (50, HEIGHT/2)
#отдельный класс для нашей машинки что бы удобно к ней обращаться

def draw(screen, player_car):
    screen.blit(DESERT, (0, 0))#отрисовка игровой карты

    player_car.draw(screen)#отрисовка машинки
    global run
    r = 0
    while r <= 29:
        if player_car.x <= (coord[r]+100) and player_car.x >= (coord[r]):
            if player_car.y <= (coord[r + 1]+100) and player_car.y >= (coord[r + 1]):
                screen.blit(text1, (WIDTH/2-100, HEIGHT/2))
                run = False
                break
        r += 2
    #проверка на пересечение машинки и препятсвий и в послующем вывод соответсвующей надписи и протокол окончания игры
    if player_car.x>= WIDTH-50:
        screen.blit(text2, (WIDTH / 2 - 100, HEIGHT / 2))
        run = False
    #проверка на пересечение машинки и финиша и в послующем вывод соответсвующей надписи и протокол окончания игры

    pygame.display.update()
    if not run:
        time.sleep(1.3)
    #временная пауза для возможности прочитать выводимую надпись

player_car = PCar()#задаем переменнуюдля обращения к нашей машинке
motion_sensor = 0#сенсор по которому будем определять вперёд или назад ехала машинка что бы коректно менять её скорость
#когда она не ускоряется

while run:
    pygame.time.Clock().tick(FPS)#используем наш фпс для оптимизации кода. именно столько раз сколько стоит у фпс будет
                                 #воспроизводиться цикл while за секунду
    draw(SCREEN, player_car)#рисуем наши обьекты кроме препядствий ведь у них нет собственного класса

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    #создаём возможность закрыть наше игровое окно

    keys = pygame.key.get_pressed()#добавляем возможность зажатия кнопки для комфортной игры
    moved = False#для того что бы определить двигаеться ли машинка в любую из сторон
    moved_up = False#для того что бы определить двигаеться ли машинка вперёд

    if keys[pygame.K_a]:
        if keys[pygame.K_w]:
            player_car.rotate(left=True)
        if keys[pygame.K_s]:
            player_car.rotate(right=True)
    #реализация поворота налево когда одновременно прожаты клавиши ускорения

    if keys[pygame.K_d]:
        if keys[pygame.K_w]:
            player_car.rotate(right=True)
        if keys[pygame.K_s]:
            player_car.rotate(left=True)
    #реализация поворота направо когда одновременно прожаты клавиши ускорения


    if keys[pygame.K_w]:
        moved = True  # определяем что машинка едет
        moved_up = True#определяем что машинка едет вперёд
        motion_sensor = 0#обнуляем сенсор, это как показатель что последние движение было совершенно вперёд
        player_car.move_manager(moved_up)#вызываем функцию которой даём понять что движение происходит вперёд
    if keys[pygame.K_s]:
        moved = True# определяем что машинка едет
        motion_sensor += 2#изменяем значения сенсора, это как показатель что последнее было совершенно назад
        player_car.move_manager(moved_up)#вызываем функцию которой даём понять что движение происходит назад
        if not moved:#условие проверяющие едет ли машинка, если нет то начинает затухание скорости
         if motion_sensor != 0:
            player_car.acceleration_speed_back()
        # если сенсор не ноль значит последним направлением движения это было назад, поэтому мы вызываем функцию которая
        #делает затухание скорости при движении назад
        else:
            player_car.acceleration_speed()
        # если сенсор ноль значит последним направлением движения это было вперёд, поэтому мы вызываем функцию которая
        # делает затухание скорости при движении вперёд

pygame.quit()