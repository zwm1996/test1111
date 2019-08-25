import pygame
import time

import self as self
from pygame.examples.headless_no_windows_needed import screen
from pygame.locals import *


# 飞机类
class HeroPlan(object):
    def __int__(self, screen):
        self.x = 200
        self.y = 280
        self.scree = screen
        self.image = pygame.image.load("./image/ship.bmp")
        self.bullet_

        #显示我方飞机

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        # 移动
    def move_left (self):
       self. x -= 5

    def move_right(self):
       self.x += 5

    def move_up(self):
       self.y -= 5

    def move_down(self):
        self.y += 5
    def fire(self):
        bullet=Bullet(self.screen,self.x,self.y)
        bullet.display()




# 子弹类
class Bullet(object):
    def __int__(self, screen,x, y):
       self.x = x+10
       self.y = y-20
       self.scree = screen
       self.image = pygame.image.load("./image/ship.bmp")
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

 # 键盘控制
def key_contrl(hero):
    for event in pygame.event.get():
        # print(event.type)
        # 判断是否点击了退出按钮
        if event.type == pygame.QUIT:
            print("exit")
            exit()
            # return ""
        # 判断是否按下键
        elif event.type == pygame.KEYDOWN:
            # 检测按键是否是a或者left
            if event.type == pygame.K_a or event.key == pygame.K_LEFT:
                print("left")

                hero.move_left()
                # 检测按键是否d或者right
            elif event.type == pygame.K_b or event.key == pygame.K_RIGHT:
                print("right")

                hero.move_right()
            elif event.type == pygame.K_w or event.key == pygame.K_UP:
                print("up")
                hero.move_up()
             elif event.type == pygame.K_x or event.key == pygame.K_DOWN:
                print("down")
                hero.move_down()
            elif event.key == K_SPACE:
               print("--space--")
               # 发射子弹
               hero.fiie()

 def main():
    # 创建窗口
    screen = pygame.display.set_mode((500, 330), 0, 32)
    # 创建背景图片
    background = pygame.image.load("./image/背景.jpg")
    # 创建飞机
    hero = HeroPlan(screen)

    while True:
        # 设定要显示的背景图
        screen.blit(background, (0, 0))
        # screen.blit(hero, (x, y))

        hero.display()
        key_contrl(hero)
        #  更新要显示的图
        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
