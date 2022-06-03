# encoding=gbk
import pygame
import random
from Button import *
from Map_Data import *
import game
import time

# �������
MAP_WIDTH = 288  # ��ͼ��С
MAP_HEIGHT = 512
FPS = 30  # ˢ����
PIPE_GAPS = [90, 100, 110, 120, 130, 140]  # ȱ�ڵľ��� ����6���������
# PIPE_GAPS1 = []
PIPE_HEIGHT_RANGE = [int(MAP_HEIGHT * 0.5), int(MAP_HEIGHT * 0.7)]  # �ܵ����ȷ�Χ
PIPE_DISTANCE = 120  # �ܵ�֮�����

# ��Ϸ��������
pygame.init()  # ���г�ʼ��
SCREEN = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))  # ���ô���������Ļ��С
pygame.display.set_caption('FLAPPY BIRD')  # ����
CLOCK = pygame.time.Clock()  # ����ʱ��

Return = Button(SCREEN,"NONE" ,"Single", 5, 15)
# �����ز�
SPRITE_FILE = '.\images\\'
# �б��Ƶ�ʽ ������ֲ�ͬ���������״̬
BIRDS = [[f'{SPRITE_FILE}{bird}bird-{move}flap.png' for move in ['up', 'mid', 'down']] for bird in ['red', 'blue', 'yellow']]
BGPICS = [SPRITE_FILE + 'background-day.png', SPRITE_FILE + 'background-night.png']
PIPES = [SPRITE_FILE + 'pipe-green.png', SPRITE_FILE + 'pipe-red.png']
NUMBERS = [f'{SPRITE_FILE}{n}.png' for n in range(10)]

# ��ͼƬ���ó�һ�����ֵ� ����ͨ��key-value�治ͬ�ĳ���ͼ
IMAGES = {}
IMAGES['numbers'] = [pygame.image.load(number) for number in NUMBERS]  # �����ز���10�� ��˱���
IMAGES['guide'] = pygame.image.load(SPRITE_FILE + 'message.png')
IMAGES['gameover'] = pygame.image.load(SPRITE_FILE + 'gameover.png')
IMAGES['floor'] = pygame.image.load(SPRITE_FILE + 'base.png')
IMAGES['title'] = pygame.image.load(SPRITE_FILE + 'title.png')

# �ذ�ĸ���һ���ܳ��õı���
FLOOR_H = MAP_HEIGHT - IMAGES['floor'].get_height()  # ��Ļ�߼�ȥfloorͼƬ�ĸ� ����������Ļ���λ��

font = pygame.font.SysFont('resources/FlappyBirdFont.ttf', 30)

# �ܵ�
Pipes = []
bird = Bird("123", "123")
# ִ�к���
def main():
    while True:
        IMAGES['bgpic'] = pygame.image.load(random.choice(BGPICS))  # random��choice��������������б��ﷵ��һ��Ԫ�� ������ߺ�ҹ
        IMAGES['bird'] = [pygame.image.load(frame) for frame in random.choice(BIRDS)]  # �б��Ƶ�ʽ ��Ҳ�����
        pipe = pygame.image.load(random.choice(PIPES))
        IMAGES['pipe'] = [pipe, pygame.transform.flip(pipe, False, True)]  # flip�Ƿ�ת ���ܵ������������ Flaseˮƽ������True���·�ת
        menu_window()
        result = game_window()


def menu_window():
    floor_gap = IMAGES['floor'].get_width() - MAP_WIDTH  # �ذ��϶ 336 - 288 = 48
    floor_x = 0

    # ����λ��
    guide_x = (MAP_WIDTH - IMAGES['guide'].get_width()) / 2
    guide_y = MAP_HEIGHT * 0.12

    # С��λ��
    bird_x = MAP_WIDTH * 0.2
    bird_y = MAP_HEIGHT * 0.5 - IMAGES['bird'][0].get_height() / 2
    bird_y_vel = 1  # С����е����� ��y��������
    max_y_shift = 50  # С����е�������
    y_shift = 0  # С����ʼ����Ϊ0

    idx = 0  # С����ɿ��Ƶ��
    frame_seq = [0] * 5 + [1] * 5 + [2] * 5 + [1] * 5  # ����С�����˶�������

    while True:

        if floor_x <= -floor_gap:  # ���ذ��ܵ��������ʱ��
            floor_x = floor_x + floor_gap  # ˢ�µذ��x��
        else:
            floor_x -= 4  # �ذ� x����ƶ��ٶ�

        if abs(y_shift) == max_y_shift:  # ���y_shift�ľ���ֵ = ������
            bird_y_vel *= -1  # ��ת����� ͬʱ�����ٶ�Ϊ1
        else:
            bird_y += bird_y_vel
        y_shift += bird_y_vel  # С��y���������� ���·�

        # С����
        idx += 1  # ���ɿ��Ƶ��
        idx %= len(frame_seq)  # ͨ��ȡ��õ� 0 1 2
        frame_index = frame_seq[idx]  # С��ͼƬ���±� ���ǳ���״̬
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
        CLOCK.tick(FPS)  # ��ÿ��30֡ˢ����Ļ


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
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # �ո��ĳ��
                flap = True

        bird.update(flap)

        for pipe in Pipes:
            print(pipe.trect.x)
            pipe.update()
        print(bird.rect.x)
        if bird.rect.y > FLOOR_H or bird.rect.y < 0:
            # ��������ʱ����� ���� �ܵ� ������ʾ�ڽ�������
            bird.go_die()
            run = False
        for pipe in Pipes:
            if pipe.trect.colliderect(bird.rect) or pipe.brect.colliderect(bird.rect):
                bird.go_die() 
                run = False

        #��С����ߴ��� �ܵ��ұ߾͵÷�
        if Pipes[0].trect.x == 56 or Pipes[1].trect.x == 56 or Pipes[1].trect.x == 54:
            bird.score += 1
        
        redrawWindow()
    gameover_x = MAP_WIDTH * 0.5 - IMAGES['gameover'].get_width() / 2
    gameover_y = MAP_HEIGHT * 0.4
    SCREEN.blit(IMAGES['gameover'], (gameover_x, gameover_y))
    time.sleep(0.5)

# ��ʾ�÷�
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