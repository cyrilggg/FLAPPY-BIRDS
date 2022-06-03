# encoding=gbk
import pygame
import random
from Button import *
from Map_Data import *
import game
import time

# 定义变量
MAP_WIDTH = 288  # 地图大小
MAP_HEIGHT = 512
FPS = 30  # 刷新率
PIPE_GAPS = [90, 100, 110, 120, 130, 140]  # 缺口的距离 有这6个随机距离
# PIPE_GAPS1 = []
PIPE_HEIGHT_RANGE = [int(MAP_HEIGHT * 0.5), int(MAP_HEIGHT * 0.7)]  # 管道长度范围
PIPE_DISTANCE = 120  # 管道之间距离

# 游戏基本设置
pygame.init()  # 进行初始化
SCREEN = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))  # 调用窗口设置屏幕大小
pygame.display.set_caption('FLAPPY BIRD')  # 标题
CLOCK = pygame.time.Clock()  # 建立时钟

Return = Button(SCREEN,"NONE" ,"Single", 5, 15)
# 加载素材
SPRITE_FILE = '.\images\\'
# 列表推导式 获得三种不同的鸟和三种状态
BIRDS = [[f'{SPRITE_FILE}{bird}bird-{move}flap.png' for move in ['up', 'mid', 'down']] for bird in ['red', 'blue', 'yellow']]
BGPICS = [SPRITE_FILE + 'background-day.png', SPRITE_FILE + 'background-night.png']
PIPES = [SPRITE_FILE + 'pipe-green.png', SPRITE_FILE + 'pipe-red.png']
NUMBERS = [f'{SPRITE_FILE}{n}.png' for n in range(10)]

# 将图片设置成一个大字典 里面通过key-value存不同的场景图
IMAGES = {}
IMAGES['numbers'] = [pygame.image.load(number) for number in NUMBERS]  # 数字素材有10张 因此遍历
IMAGES['guide'] = pygame.image.load(SPRITE_FILE + 'message.png')
IMAGES['gameover'] = pygame.image.load(SPRITE_FILE + 'gameover.png')
IMAGES['floor'] = pygame.image.load(SPRITE_FILE + 'base.png')
IMAGES['title'] = pygame.image.load(SPRITE_FILE + 'title.png')

# 地板的高是一个很常用的变量
FLOOR_H = MAP_HEIGHT - IMAGES['floor'].get_height()  # 屏幕高减去floor图片的高 就是他在屏幕里的位置

font = pygame.font.SysFont('resources/FlappyBirdFont.ttf', 30)

# 管道
Pipes = []
bird = Bird("123", "123")
# 执行函数
def main():
    while True:
        IMAGES['bgpic'] = pygame.image.load(random.choice(BGPICS))  # random的choice方法可以随机从列表里返回一个元素 白天或者黑夜
        IMAGES['bird'] = [pygame.image.load(frame) for frame in random.choice(BIRDS)]  # 列表推导式 鸟也是随机
        pipe = pygame.image.load(random.choice(PIPES))
        IMAGES['pipe'] = [pipe, pygame.transform.flip(pipe, False, True)]  # flip是翻转 将管道放下面和上面 Flase水平不动，True上下翻转
        menu_window()
        result = game_window()


def menu_window():
    floor_gap = IMAGES['floor'].get_width() - MAP_WIDTH  # 地板间隙 336 - 288 = 48
    floor_x = 0

    # 标题位置
    guide_x = (MAP_WIDTH - IMAGES['guide'].get_width()) / 2
    guide_y = MAP_HEIGHT * 0.12

    # 小鸟位置
    bird_x = MAP_WIDTH * 0.2
    bird_y = MAP_HEIGHT * 0.5 - IMAGES['bird'][0].get_height() / 2
    bird_y_vel = 1  # 小鸟飞行的速率 按y坐标向下
    max_y_shift = 50  # 小鸟飞行的最大幅度
    y_shift = 0  # 小鸟起始幅度为0

    idx = 0  # 小鸟翅膀煽动频率
    frame_seq = [0] * 5 + [1] * 5 + [2] * 5 + [1] * 5  # 控制小鸟翅膀运动上中下

    while True:

        if floor_x <= -floor_gap:  # 当地板跑到最大间隔的时候
            floor_x = floor_x + floor_gap  # 刷新地板的x轴
        else:
            floor_x -= 4  # 地板 x轴的移动速度

        if abs(y_shift) == max_y_shift:  # 如果y_shift的绝对值 = 最大幅度
            bird_y_vel *= -1  # 调转方向飞 同时飞行速度为1
        else:
            bird_y += bird_y_vel
        y_shift += bird_y_vel  # 小鸟y轴正负交替 上下飞

        # 小鸟翅膀
        idx += 1  # 翅膀煽动频率
        idx %= len(frame_seq)  # 通过取余得到 0 1 2
        frame_index = frame_seq[idx]  # 小鸟图片的下标 就是翅膀的状态
        SCREEN.blit(IMAGES['bgpic'], (0, 0))
        SCREEN.blit(IMAGES['floor'], (floor_x, FLOOR_H))
        SCREEN.blit(IMAGES['guide'], (guide_x, guide_y))
        SCREEN.blit(IMAGES['bird'][frame_index], (bird_x, bird_y))
        
        Return.draw_image()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(mouse_x, mouse_y)
                if Return.image_rect.collidepoint(mouse_x, mouse_y):
                    game.main_title()
        pygame.display.update()
        CLOCK.tick(FPS)  # 以每秒30帧刷新屏幕


def game_window():
    global Pipes, bird
    Pipes.clear()

    Pipe1 = Pipe(MAP_WIDTH)
    Pipe2 = Pipe(MAP_WIDTH + 170)
    Pipes.append(Pipe1)
    Pipes.append(Pipe2)
    bird = Bird("123", "123")
    run = True
    while run:
        flap = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # 空格拍翅膀
                flap = True

        bird.update(flap)

        for pipe in Pipes:
            print(pipe.trect.x)
            pipe.update()
        print(bird.rect.x)
        if bird.rect.y > FLOOR_H or bird.rect.y < 0:
            # 保存死亡时的鸟儿 分数 管道 继续显示在结束窗口
            bird.go_die()
            run = False
        for pipe in Pipes:
            if pipe.trect.colliderect(bird.rect) or pipe.brect.colliderect(bird.rect):
                bird.go_die() 
                run = False

        #当小鸟左边大于 管道右边就得分
        if Pipes[0].trect.x == 56 or Pipes[1].trect.x == 56 or Pipes[1].trect.x == 54:
            bird.score += 1
        
        redrawWindow()
    gameover_x = MAP_WIDTH * 0.5 - IMAGES['gameover'].get_width() / 2
    gameover_y = MAP_HEIGHT * 0.4
    SCREEN.blit(IMAGES['gameover'], (gameover_x, gameover_y))
    time.sleep(0.5)

# 显示得分
def show_score(score):
    score_str = str(score)
    w = IMAGES['numbers'][0].get_width()
    x = MAP_WIDTH / 2 - 2 * w / 2
    y = MAP_HEIGHT * 0.1
    for number in score_str:  # IMAGES['numbers'] = [pygame.image.load(number) for number in NUMBERS]
        SCREEN.blit(IMAGES['numbers'][int(number)], (x, y))
        x += w

def redrawWindow():
    global Pipes, bird
    SCREEN.blit(IMAGES['bgpic'], (0, 0))
    gameover_x = MAP_WIDTH * 0.5 - IMAGES['gameover'].get_width() / 2
    gameover_y = MAP_HEIGHT * 0.4
    
    for pipe in Pipes:
        SCREEN.blit(IMAGES['pipe'][0], pipe.trect)
        SCREEN.blit(IMAGES['pipe'][1], pipe.brect)
        
        #print(pipe.trect.x)
    SCREEN.blit(IMAGES['floor'], (0, FLOOR_H))     
    Return.draw_image()
            
    show_score(bird.score)
    
    if bird.gameover:
        GameState = 1
    if (bird.gamestate2):
        count_down(Map)
        return
    if (bird.gamestate1):
        SCREEN.blit(IMAGES['gameover'], (gameover_x, gameover_y))
        GameState = 0

    SCREEN.blit(pygame.transform.rotate(IMAGES['bird'][bird.frame_list[bird.frame_index]], bird.rotate), bird.rect)
    
    pygame.display.update()

    CLOCK.tick(FPS)

if __name__ == '__main__':
    main()