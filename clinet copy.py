#coding: gbk
import socket               # 导入 socket 模块
import pygame
import random
import time
from network import *

######################################## 游戏基本设置
pygame.init()  # 进行初始化
SCREEN = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))  # 调用窗口设置屏幕大小
CLOCK = pygame.time.Clock()  # 建立时钟
Own_Ip = socket.gethostbyname(socket.gethostname())#得到本地ip

pygame.display.set_caption("clinet")

def show_score(score):
    score_str = str(score)
    w = IMAGES['numbers'][0].get_width()
    x = MAP_WIDTH / 2 - 2 * w / 2
    y = MAP_HEIGHT * 0.1
    for number in score_str:  # IMAGES['numbers'] = [pygame.image.load(number) for number in NUMBERS]
        SCREEN.blit(IMAGES['numbers'][int(number)], (x, y))
        x += w

def redrawWindow(Map):
    SCREEN.blit(IMAGES['bgpic'], (0, 0))
    gameover_x = MAP_WIDTH * 0.5 - IMAGES['gameover'].get_width() / 2
    gameover_y = MAP_HEIGHT * 0.4
    print(FLOOR_H, MAP_HEIGHT,IMAGES['floor'].get_height())
    
    for pipe in Map.Pipes:
        SCREEN.blit(IMAGES['pipe'][0], pipe.trect)
        SCREEN.blit(IMAGES['pipe'][1], pipe.brect)
    SCREEN.blit(IMAGES['floor'], (0, FLOOR_H))     
    
    for bird in Map.Birds:
        if bird.ip == Own_Ip:
            show_score(Map.Birds[0].score)
        SCREEN.blit(pygame.transform.rotate(IMAGES['bird'][bird.frame_list[bird.frame_index]], bird.rotate), bird.rect)
    
    if (bird.gameover):
        SCREEN.blit(IMAGES['gameover'], (gameover_x, gameover_y))
    pygame.display.update()
    
    CLOCK.tick(FPS)

def connect():
    global Own_Ip
    pygame.init()
    run = True
    n = Network()
    p = n.getP()
    Own_Ip = p#获取连接到服务器时自己的客户端地址
    clock = pygame.time.Clock()
    
    while run:
        print("Successs")
        clock.tick(60)
        d = Data()
        
        d.ip = n.addr[0]
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            d.up = 1
        if keys[pygame.K_RCTRL] or keys[pygame.K_LCTRL]:
            d.prop = 1
        
        mp = n.send(d)
        print(mp)
        redrawWindow(mp)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


        

if __name__ == '__main__':
    connect()