#coding: gbk
import socket               # 导入 socket 模块
import pygame
import random
import time
import Map_Data
import game
from network import *
from Button import *
name = "123"
ip = "127.0.0.1"

# 游戏基本设置
pygame.init()  # 进行初始化
font = pygame.font.SysFont('resources/FlappyBirdFont.ttf', 30)

SCREEN = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))  # 调用窗口设置屏幕大小
CLOCK = pygame.time.Clock()  # 建立时钟
Own_Ip = socket.gethostbyname(socket.gethostname())#得到本地ip

pygame.display.set_caption("clinet")

GameState = 0
GameStart = 0

Return = Button(SCREEN,"NONE" ,"Single", 5, 15)
def show_score(score):
    score_str = str(score)
    w = IMAGES['numbers'][0].get_width()
    x = MAP_WIDTH / 2 - 2 * w / 2
    y = MAP_HEIGHT * 0.1
    for number in score_str:  # IMAGES['numbers'] = [pygame.image.load(number) for number in NUMBERS]
        SCREEN.blit(IMAGES['numbers'][int(number)], (x, y))
        x += w


def count_down(Map):
    w = IMAGES['numbers'][0].get_width()
    x = MAP_WIDTH / 2 - 2 * w / 2
    y = MAP_HEIGHT * 0.1
    for i in range(3, 0, -1):  # IMAGES['numbers'] = [pygame.image.load(number) for number in NUMBERS]
        SCREEN.blit(IMAGES['bgpic'], (0, 0))
        gameover_x = MAP_WIDTH * 0.5 - IMAGES['gameover'].get_width() / 2
        gameover_y = MAP_HEIGHT * 0.4
        
        for pipe in Map.Pipes:
            SCREEN.blit(IMAGES['pipe'][0], pipe.trect)
            SCREEN.blit(IMAGES['pipe'][1], pipe.brect)
        SCREEN.blit(IMAGES['floor'], (0, FLOOR_H))     
        
        for bird in Map.Birds:
            SCREEN.blit(pygame.transform.rotate(IMAGES['bird'][bird.frame_list[bird.frame_index]], bird.rotate), bird.rect)
            text_namerect = font.render(bird.name,True,(255,255,255)).get_rect()
            text_namerect.y = bird.rect.y - 30
            text_namerect.x = bird.rect.x
            SCREEN.blit(font.render(bird.name,True,(0, 0, 0)), text_namerect)
        
        SCREEN.blit(IMAGES['numbers'][i], (x, y))
        time.sleep(0.5)
        pygame.display.update()
        CLOCK.tick(FPS)
    time.sleep(0.5)
    GameStart = 1

def redrawWindow(Map):
    global GameState
    SCREEN.blit(IMAGES['bgpic'], (0, 0))
    gameover_x = MAP_WIDTH * 0.5 - IMAGES['gameover'].get_width() / 2
    gameover_y = MAP_HEIGHT * 0.4
    
    for pipe in Map.Pipes:
        SCREEN.blit(IMAGES['pipe'][0], pipe.trect)
        SCREEN.blit(IMAGES['pipe'][1], pipe.brect)
        
        #print(pipe.trect.x)
    SCREEN.blit(IMAGES['floor'], (0, FLOOR_H))     
    Return.draw_image()
    for bird in Map.Birds:
        if bird.ip == Own_Ip:
            if bird.invincibility_time > 0:
                print(str(bird.invincibility_time))
                text_namerect = font.render(str(bird.invincibility_time),True,(255,255,255)).get_rect()
                text_namerect.y = 470
                text_namerect.x = 240
                SCREEN.blit(font.render(str(bird.invincibility_time),True,(0, 0, 255)), text_namerect)
        
            #print(bird.rect.x)
            if not GameStart:
                show_score(Map.Birds[0].score)
            #print(bird.gamestate1, bird.gamestate2)
            if bird.gameover:
                GameState = 1
            if (bird.gamestate2):
                count_down(Map)
                return
            if (bird.gamestate1):
                SCREEN.blit(IMAGES['gameover'], (gameover_x, gameover_y))
                GameState = 0

        SCREEN.blit(pygame.transform.rotate(IMAGES['bird'][bird.frame_list[bird.frame_index]], bird.rotate), bird.rect)
        text_namerect = font.render(bird.name,True,(255,255,255)).get_rect()
        text_namerect.y = bird.rect.y - 30
        text_namerect.x = bird.rect.x
        SCREEN.blit(font.render(bird.name,True,(0, 0, 0)), text_namerect)
        
        pygame.display.update()
    
    CLOCK.tick(FPS)

def connect():
    global name, ip
    name = input("Please input your name : ")
    ip = input("Please input the host ip you want to join : ")
    global Own_Ip, GameState
    pygame.init()
    run = True
    n = Network(ip)
    n.connect()
    
    n.send_msg_to_server(name)
    Own_Ip = n.recieve_msg()#获取连接到服务器时自己的客户端地址
    clock = pygame.time.Clock()
    
    while run:
        #print("Successs")
        clock.tick(60)
        d = Data()
        
        d.ip = Own_Ip
        keys = pygame.key.get_pressed()
        d.gameover = GameState
        if keys[pygame.K_SPACE]:
            d.up = 1
        if keys[pygame.K_RCTRL] or keys[pygame.K_LCTRL]:
            d.prop = 1
        
        mp = n.send(d)
        #print(mp)
        #print(d.up)
        redrawWindow(mp)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(mouse_x, mouse_y)
                if Return.image_rect.collidepoint(mouse_x, mouse_y):#是不是按到回去了
                    n.close()
                    game.main_title()

        

if __name__ == '__main__':
    connect()