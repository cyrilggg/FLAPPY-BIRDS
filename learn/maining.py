# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 17:03:52 2022

@author: leslie
"""

import pygame
import sys
import random

class Pipes(object):
    def __init__(self):
        self.bar_up = pygame.image.load("C:/Users/leslie/Desktop/bar_down.png");
        self.bar_down = pygame.image.load("C:/Users/leslie/Desktop/bar_up.png");
        self.pipe_x = 400;
        self.pipe_y1 = random.randint(-350,-300)
        self.pipe_y2 = random.randint(400,500)
        
    def update_pipe(self):
        self.pipe_x -= 2
        if self.pipe_x < -80:
            global score
            score += 1
            self.pipe_x = 400
            self.pipe_y1 = random.randint(-350,-100)
            self.pipe_y2 = random.randint(430,550)
            #self.pipe_y2 = self.pipe_y1 + 700

class Bird():
    def  __init__(self):
        self.birdsize=pygame.Rect(65,50,40,40)
        self.birds = [
                    pygame.image.load("C:/Users/leslie/Desktop/bird1.png"),
                    pygame.image.load("C:/Users/leslie/Desktop/bird2.png"),
                    pygame.image.load("C:/Users/leslie/Desktop/bird3.png"),
                    pygame.image.load("C:/Users/leslie/Desktop/dead.png")
                    ]
        self.stutas = 0 
        self.bird_x = 120
        self.bird_y = 350
        self.jump = False    
        self.jumpSpeed = 1.5  
        self.downing = 1.5   
        self.dead = False    
    
    def update_bird(self):
        if self.jump:
            self.bird_y -= self.jumpSpeed
        else:
            self.bird_y +=self.downing
        self.birdsize[1] = self.bird_y


def map_view():
   
    screen.fill('white')
    screen.blit(background, (0, 0))
   
    screen.blit(Pipes.bar_up, (Pipes.pipe_x, Pipes.pipe_y1))
    screen.blit(Pipes.bar_down, (Pipes.pipe_x, Pipes.pipe_y2))
    Pipes.update_pipe()
    
    if Bird.jump:
        Bird.stutas=1
    elif Bird.dead:
        Bird.stutas=3
    else:
        Bird.stutas=2
    screen.blit(Bird.birds[Bird.stutas],(Bird.bird_x,Bird.bird_y))
    Bird.update_bird()
    
    screen.blit(font.render('sorce:' + str(score), -1, (20, 20, 200)), (100, 50))
    pygame.display.update()  
    
    
def PZ_test():
    up_bar = pygame.Rect(Pipes.pipe_x,Pipes.pipe_y1,Pipes.bar_up.get_width()-10 ,Pipes.bar_up.get_height())
    down_bar = pygame.Rect(Pipes.pipe_x,Pipes.pipe_y2,Pipes.bar_down.get_width()-10,Pipes.bar_down.get_height())

    if up_bar.colliderect(Bird.birdsize) or down_bar.colliderect(Bird.birdsize):
        Bird.dead = True
        return True
    elif  Bird.birdsize[1] > height or Bird.birdsize[1]<0:
        Bird.dead = True
        return True
    else:
        return False
    
def end_map():
    
    screen.blit(background, (0, 0))
    text1 = "Game Over"
    text2 = "final score:  " + str(score)
    ft1_surf = font.render(text1, 1, 'green')                            
    ft2_surf = font.render(text2, 1, 'red')                            
    screen.blit(ft1_surf, [screen.get_width() / 2 - ft1_surf.get_width() / 2, 100])  
    screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 200]) 
    pygame.display.flip()                                                           

    

if __name__ == '__main__':
    pygame.init()                            
    pygame.font.init()                       
    pygame.display.set_caption("123")
    size = width, height = 350, 600         
    screen = pygame.display.set_mode(size) 
    font = pygame.font.SysFont("ziti.ttf", 50)  
    clock = pygame.time.Clock() 
    Bird = Bird()
    Pipes = Pipes()
    score=0
    
    while True:
        clock.tick(80) 
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if event.type == pygame.KEYDOWN and Bird.dead==False:
                   if event.key == pygame.K_UP:
                       Bird.jump = True                              
                                   
                   if event.key == pygame.K_DOWN:
                       Bird.jump = False             
                                          
        background = pygame.image.load("C:/Users/leslie/Desktop/background.jpg")
        if PZ_test():
            end_map()
        else:
            map_view()
            
    pygame.quit() 






   