# encoding=gbk
import Single
import client 
from Map_Data import *
from Button import *
import pygame
import random

# 游戏基本设置
font = pygame.font.SysFont('resources/FlappyBirdFont.ttf', 30)

SCREEN = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))  # 调用窗口设置屏幕大小
CLOCK = pygame.time.Clock()  # 建立时钟

pygame.display.set_caption("flappybirds")       
single = Button(SCREEN,"NONE" ,"Single", 90, 270)
multiplayer = Button(SCREEN,"NONE" ,"Multy", 90, 330)

#游戏界面
#包含 多人游戏，单人游戏，以及游戏设置
def main_title():
    floor_x = 0
    floor_gap = IMAGES['floor'].get_width() - MAP_WIDTH  # 地板间隙 336 - 288 = 48
   
    while(True):
        if floor_x <= -floor_gap:  # 当地板跑到最大间隔的时候
            floor_x = floor_x + floor_gap  # 刷新地板的x轴
        else:
            floor_x -= 0.5  # 地板 x轴的移动速度
        SCREEN.blit(IMAGES['bgpic'], (0, 0))
        SCREEN.blit(IMAGES['floor'], (floor_x, FLOOR_H))
        SCREEN.blit(IMAGES['title'], (52.0, 61.44))
        single.draw()
        multiplayer.draw()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(mouse_x, mouse_y, single.rect)
                if single.rect.collidepoint(mouse_x, mouse_y):
                    single_type()
                if multiplayer.rect.collidepoint(mouse_x, mouse_y):
                    multi_type()

        pygame.display.update()

#单人模式
def single_type():
    Single.main()

#多人模式
def multi_type():
    client.connect()

#设置
#详见setting.py
#界面有 设置皮肤 设置名字 调整声音大小 调整音效大小
def setting():
    pass
    setting.py()
    dress()

if __name__ == '__main__':
    main_title()


