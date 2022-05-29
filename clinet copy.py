#coding: gbk
import socket               # ���� socket ģ��
import pygame
import random
from network import *

######################################## ��Ϸ��������
pygame.init()  # ���г�ʼ��
SCREEN = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))  # ���ô���������Ļ��С
CLOCK = pygame.time.Clock()  # ����ʱ��

pygame.display.set_caption("clinet")

index = 0
def redrawWindow(Map):
    global index
    SCREEN.blit(IMAGES['bgpic'], (0, 0))
    gameover_x = MAP_WIDTH * 0.5 - IMAGES['gameover'].get_width() / 2
    gameover_y = MAP_HEIGHT * 0.4
    
    for bird in Map.Birds:
        bird.go_die()
        SCREEN.blit(bird.image, bird.rect)
    
    for pipe in Map.Pipes:
        SCREEN.blit(IMAGES['pipe'][0], pipe.trect)
        SCREEN.blit(IMAGES['pipe'][1], pipe.brect)
        
    SCREEN.blit(IMAGES['floor'], (0, FLOOR_H))
    SCREEN.blit(IMAGES['gameover'], (gameover_x, gameover_y))
    pygame.display.update()
    
    CLOCK.tick(FPS)

def connect():
    pygame.init()
    run = True
    n = Network()
    p = n.getP()
    print(type(p))
    redrawWindow(p)
    clock = pygame.time.Clock()
    
    while run:
        print("Successs")
        clock.tick(60)
        d = Data()
        
        d.ip = n.addr
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            d.up = 1
        if keys[pygame.K_RCTRL] or keys[pygame.K_LCTRL]:
            d.prop = 1
        
        mp = n.send(d)
        redrawWindow(mp)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        

if __name__ == '__main__':
    connect()