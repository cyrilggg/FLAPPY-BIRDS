# encoding=gbk
import Single
import client 
from Map_Data import *
from Button import *
import pygame
import random

# ��Ϸ��������
font = pygame.font.SysFont('resources/FlappyBirdFont.ttf', 30)

SCREEN = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))  # ���ô���������Ļ��С
CLOCK = pygame.time.Clock()  # ����ʱ��

pygame.display.set_caption("flappybirds")       
single = Button(SCREEN,"NONE" ,"Single", 90, 270)
multiplayer = Button(SCREEN,"NONE" ,"Multy", 90, 330)

#��Ϸ����
#���� ������Ϸ��������Ϸ���Լ���Ϸ����
def main_title():
    floor_x = 0
    floor_gap = IMAGES['floor'].get_width() - MAP_WIDTH  # �ذ��϶ 336 - 288 = 48
   
    while(True):
        if floor_x <= -floor_gap:  # ���ذ��ܵ��������ʱ��
            floor_x = floor_x + floor_gap  # ˢ�µذ��x��
        else:
            floor_x -= 0.5  # �ذ� x����ƶ��ٶ�
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

#����ģʽ
def single_type():
    Single.main()

#����ģʽ
def multi_type():
    client.connect()

#����
#���setting.py
#������ ����Ƥ�� �������� ����������С ������Ч��С
def setting():
    pass
    setting.py()
    dress()

if __name__ == '__main__':
    main_title()


