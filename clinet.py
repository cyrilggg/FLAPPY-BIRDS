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

def redrawWindow(Map):
    for bird in Map.Birds:
        bird.go_die()
        SCREEN.blit(bird.image, bird.rect)
    
    SCREEN.blit(IMAGES['bgpic'], (0, 0))
    pipe_group.draw(SCREEN)
    SCREEN.blit(IMAGES['floor'], (0, FLOOR_H))
    SCREEN.blit(IMAGES['gameover'], (gameover_x, gameover_y))
    show_score(result['score'])
    pygame.display.update()
    CLOCK.tick(FPS)

def connect():
    pygame.init()
    run = True
    n = Network()
    p = n.getP()
    redrawWindow(p)
    clock = pygame.time.Clock()
    
    while run:
        print("Successs")
        clock.tick(60)
        mp = n.send(p)
        redrawWindow(p)
        print(mp.Birds[0].ip)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p = Data()
        
        p.ip = socket.gethostbyname(socket.gethostname())
        keys = pygame.key.get_pressed ()
        
        if keys[pygame.K_SPACE]:
            p.up = 1
        if keys[pygame.K_RCTRL] or keys[pygame.K_LCTRL]:
            p.prop = 1

if __name__ == '__main__':
    connect()