import pygame
from pygame.locals import *
import time


class HeroPlane(object):
    def __init__(self, screen):
        self.x = 190
        self.y = 700
        self.image = pygame.image.load("./image/hero1.png")
        self.screen = screen
        self.bullets = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.move()
            bullet.display()

    def fire(self):
        self.bullets.append(Bullet(self.screen, self.x, self.y))

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def move_up(self):
        self.y -= 5

    def move_down(self):
        self.y += 5


class Bullet(object):
    def __init__(self, screen, x, y, ):
        self.x = x + 41
        self.y = y - 22
        self.screen = screen
        self.image = pygame.image.load("./image/bullet.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 4


def game_control(hero_temp):
    # 获取事件，比如按键等
    for event in pygame.event.get():
        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            # 检测按键是否是w或者up
            elif event.key == K_w or event.key == K_UP:
                print("up")
                hero_temp.move_up()
            # 检测按键是否是s或者down
            elif event.key == K_s or event.key == K_DOWN:
                print("down")
                hero_temp.move_down()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                # 发射子弹
                hero_temp.fire()


def main():
    screen = pygame.display.set_mode((480, 852), 0, 32)
    background = pygame.image.load("./image/background.png")

    hero = HeroPlane(screen)

    while True:
        screen.blit(background, (0, 0))

        hero.display()

        pygame.display.update()

        game_control(hero)

        time.sleep(0.01)


if __name__ == "__main__":
    main()
