# encoding=gbk
from Map_Data import *

######################################## 游戏基本设置
pygame.init()  # 进行初始化
SCREEN = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))  # 调用窗口设置屏幕大小
CLOCK = pygame.time.Clock()  # 建立时钟

pygame.display.set_caption("clinet")

Map = newMap()

def redrawWindow(Map):
    SCREEN.blit(IMAGES['bgpic'], (0, 0))
    gameover_x = MAP_WIDTH * 0.5 - IMAGES['gameover'].get_width() / 2
    gameover_y = MAP_HEIGHT * 0.4
    
    for bird in Map.Birds:
        bird.go_die()
        SCREEN.blit(pygame.transform.rotate(IMAGES['bird'][bird.frame_list[bird.frame_index]], bird.rotate), bird.rect)
    
    for pipe in Map.Pipes:
        SCREEN.blit(IMAGES['pipe'][0], pipe.trect)
        SCREEN.blit(IMAGES['pipe'][1], pipe.brect)
        
    SCREEN.blit(IMAGES['floor'], (0, FLOOR_H))
    SCREEN.blit(IMAGES['gameover'], (gameover_x, gameover_y))
    pygame.display.update()
    
    CLOCK.tick(FPS)

if __name__ == '__main__':
    bird = Bird('127.0.0.1')
    Map.Birds.append(bird)
    
    Pipe1 = Pipe(MAP_WIDTH)
    Pipe2 = Pipe(MAP_WIDTH + PIPE_DISTANCE)
    Map.Pipes.append(Pipe1)
    Map.Pipes.append(Pipe2)
    redrawWindow(Map)