# encoding=gbk
import pygame
import random

# �������
MAP_WIDTH = 288  # ��ͼ��С
MAP_HEIGHT = 512
FPS = 60  # ˢ����
PIPE_GAPS = [180, 190, 150, 160, 145, 140]  # ȱ�ڵľ��� ����6���������
PIPE_HEIGHT_RANGE = [int(MAP_HEIGHT * 0.4), int(MAP_HEIGHT * 0.7)]  # �ܵ����ȷ�Χ
PIPE_DISTANCE = 160  # �ܵ�֮�����

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
IMAGES['bgpic'] = pygame.image.load(random.choice(BGPICS))  # random��choice��������������б��ﷵ��һ��Ԫ�� ������ߺ�ҹ
IMAGES['title'] = pygame.image.load(SPRITE_FILE + 'title.png')
IMAGES['notready'] = pygame.image.load(SPRITE_FILE + 'notready.png')
IMAGES['ready'] = pygame.image.load(SPRITE_FILE + 'ready.png')

FLOOR_H = MAP_HEIGHT - IMAGES['floor'].get_height() 

IMAGES['bird'] = [pygame.image.load(frame) for frame in random.choice(BIRDS)]  # �б��Ƶ�ʽ ��Ҳ�����

pipe = pygame.image.load(random.choice(PIPES))
IMAGES['pipe'] = [pipe, pygame.transform.flip(pipe, False, True)] 

class Pipe():
    def __init__(self, x):
        self.x_vel = -4  # �ܵ��ƶ��ٶ�

        self.trect = IMAGES['pipe'][0].get_rect()
        self.trect.top = random.randint(PIPE_HEIGHT_RANGE[0], PIPE_HEIGHT_RANGE[1])
        self.trect.x = x
        self.brect = IMAGES['pipe'][1].get_rect()
        self.brect.bottom = self.trect.top - random.choice(PIPE_GAPS)
        self.brect.x = x
        
    def update(self):
        
        self.trect.x += self.x_vel  # �ܵ�x����ƶ��ٶ�
        self.brect.x += self.x_vel
        if self.trect.x < -IMAGES['pipe'][1].get_width():
            self.trect.top = random.randint(PIPE_HEIGHT_RANGE[0], PIPE_HEIGHT_RANGE[1])
            self.brect.bottom = self.trect.top - random.choice(PIPE_GAPS)
            self.trect.x = MAP_WIDTH
            self.brect.x = MAP_WIDTH
            return True
        return False

class Bird():
        def __init__(self, addr, name):
            self.name = name
            self.frame_list = [0] * 5 + [1] * 5 + [2] * 5 + [1] * 5  # ����С�����˶�������
            self.frame_index = 0
            self.y_vel = -10  # y������ٶ�
            self.max_y_vel = 15  # y����������ٶ�
            self.rotate = 0  # �Դ�����
            self.rotate_vel = -3  # ת���ٶ�
            self.max_rotate = -30  # ���ת���ٶ�
            self.flap_rotate = 45  # ���˿ո�ֻ���Դ�������30��

            self.rect = pygame.transform.rotate(IMAGES['bird'][self.frame_list[self.frame_index]], self.rotate).get_rect()  # ����ľ���
            self.rect.x = MAP_WIDTH * 0.2
            self.rect.y = MAP_HEIGHT * 0.5 - IMAGES['bird'][0].get_height() / 2
            self.gravity = 1  # ����
            self.gameover = 0
            self.flap_acc = -10  # ����Ĵ����Ϸ� y����-10
            
            #���ߡ����޵�ʱ��
            self.invincibility_time = 0

            #00 δ��ʼ 01 ��ʼ�� 10 һ��ʼ 11 ����
            self.gamestate1 = 0
            self.gamestate2 = 0
            self.gameover = 0

            self.curstate = False
            self.surstate = False
            
            self.ready = False

            self.ip = addr

            self.color = random.choice(BIRDS) #�������ɫ

            self.score = 0
            self.score_updated = 0

        def update(self, flap=False):
            if flap:
                self.y_vel = self.flap_acc  # �Ĵ��� ��y�ٶ�-10����
                self.rotate = self.flap_rotate
            else:
                self.rotate = self.rotate + self.rotate_vel

            self.y_vel = min(self.y_vel + self.gravity, self.max_y_vel)
            self.rect.y += self.y_vel  # С�������ƶ��ľ���
            self.rorate = max(self.rotate + self.rotate_vel, self.max_rotate)

            if self.invincibility_time > 0:
                self.invincibility_time -= 1
            self.frame_index += 1  # �ȳ�������
            self.frame_index %= len(self.frame_list)  # 0~20
            if self.rect.y >= FLOOR_H:
                self.rect.y = FLOOR_H
                self.gameover = 1
                

        def go_die(self):
            if self.rect.y < FLOOR_H:
                self.y_vel = self.max_y_vel
                self.rect.y += self.y_vel
                self.rotate = -90

class newMap():
    def __init__(self):
        self.Pipes = []
        self.Birds = []

class Data():
    def __init__(self):
        self.ip = 9
        self.up = 0
        self.prop = 0
        self.gameover = 0