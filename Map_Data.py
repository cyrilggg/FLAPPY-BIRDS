# encoding=gbk
import pygame
import random

# 定义变量
MAP_WIDTH = 288  # 地图大小
MAP_HEIGHT = 512
FPS = 60  # 刷新率
PIPE_GAPS = [180, 190, 150, 160, 145, 140]  # 缺口的距离 有这6个随机距离
PIPE_HEIGHT_RANGE = [int(MAP_HEIGHT * 0.4), int(MAP_HEIGHT * 0.7)]  # 管道长度范围
PIPE_DISTANCE = 160  # 管道之间距离

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
IMAGES['bgpic'] = pygame.image.load(random.choice(BGPICS))  # random的choice方法可以随机从列表里返回一个元素 白天或者黑夜
IMAGES['title'] = pygame.image.load(SPRITE_FILE + 'title.png')
IMAGES['notready'] = pygame.image.load(SPRITE_FILE + 'notready.png')
IMAGES['ready'] = pygame.image.load(SPRITE_FILE + 'ready.png')

FLOOR_H = MAP_HEIGHT - IMAGES['floor'].get_height() 

IMAGES['bird'] = [pygame.image.load(frame) for frame in random.choice(BIRDS)]  # 列表推导式 鸟也是随机

pipe = pygame.image.load(random.choice(PIPES))
IMAGES['pipe'] = [pipe, pygame.transform.flip(pipe, False, True)] 

class Pipe():
    def __init__(self, x):
        self.x_vel = -4  # 管道移动速度

        self.trect = IMAGES['pipe'][0].get_rect()
        self.trect.top = random.randint(PIPE_HEIGHT_RANGE[0], PIPE_HEIGHT_RANGE[1])
        self.trect.x = x
        self.brect = IMAGES['pipe'][1].get_rect()
        self.brect.bottom = self.trect.top - random.choice(PIPE_GAPS)
        self.brect.x = x
        
    def update(self):
        
        self.trect.x += self.x_vel  # 管道x轴加移动速度
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
            self.frame_list = [0] * 5 + [1] * 5 + [2] * 5 + [1] * 5  # 控制小鸟翅膀运动上中下
            self.frame_index = 0
            self.y_vel = -10  # y坐标的速度
            self.max_y_vel = 15  # y轴下落最大速度
            self.rotate = 0  # 脑袋朝向
            self.rotate_vel = -3  # 转向速度
            self.max_rotate = -30  # 最大转向速度
            self.flap_rotate = 45  # 按了空格只会脑袋朝向上30度

            self.rect = pygame.transform.rotate(IMAGES['bird'][self.frame_list[self.frame_index]], self.rotate).get_rect()  # 鸟儿的矩形
            self.rect.x = MAP_WIDTH * 0.2
            self.rect.y = MAP_HEIGHT * 0.5 - IMAGES['bird'][0].get_height() / 2
            self.gravity = 1  # 重力
            self.gameover = 0
            self.flap_acc = -10  # 翅膀拍打往上飞 y坐标-10
            
            #道具——无敌时间
            self.invincibility_time = 0

            #00 未开始 01 开始中 10 一开始 11 结束
            self.gamestate1 = 0
            self.gamestate2 = 0
            self.gameover = 0

            self.curstate = False
            self.surstate = False
            
            self.ready = False

            self.ip = addr

            self.color = random.choice(BIRDS) #随机鸟颜色

            self.score = 0
            self.score_updated = 0

        def update(self, flap=False):
            if flap:
                self.y_vel = self.flap_acc  # 拍打翅膀 则y速度-10向上
                self.rotate = self.flap_rotate
            else:
                self.rotate = self.rotate + self.rotate_vel

            self.y_vel = min(self.y_vel + self.gravity, self.max_y_vel)
            self.rect.y += self.y_vel  # 小鸟向上移动的距离
            self.rorate = max(self.rotate + self.rotate_vel, self.max_rotate)

            if self.invincibility_time > 0:
                self.invincibility_time -= 1
            self.frame_index += 1  # 扇翅膀的速率
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