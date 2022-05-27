# encoding=gbk
import pygame
import random

######################################## 定义变量
MAP_WIDTH = 288  # 地图大小
MAP_HEIGHT = 512
FPS = 30  # 刷新率
PIPE_GAPS = [90, 100, 110, 120, 130, 140]  # 缺口的距离 有这6个随机距离
# PIPE_GAPS1 = []
PIPE_HEIGHT_RANGE = [int(MAP_HEIGHT * 0.5), int(MAP_HEIGHT * 0.7)]  # 管道长度范围
PIPE_DISTANCE = 120  # 管道之间距离

######################################## 加载素材
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

# 地板的高是一个很常用的变量 因此我们专门拿出来
FLOOR_H = MAP_HEIGHT - IMAGES['floor'].get_height()  # 屏幕高减去floor图片的高 就是他在屏幕里的位置

IMAGES['bird'] = [pygame.image.load(frame) for frame in random.choice(BIRDS)]  # 列表推导式 鸟也是随机
pipe = pygame.image.load(random.choice(PIPES))
IMAGES['pipe'] = [pipe, pygame.transform.flip(pipe, False, True)] 

class Pipe():
    def __init__(self, x):
        self.x_vel = -4  # 管道移动速度

        self.timage = IMAGES['pipe'][0]
        self.trect = self.timage.get_rect()
        self.trect.x = x
        self.trect.top = random.randint(PIPE_HEIGHT_RANGE[0], PIPE_HEIGHT_RANGE[1])
        
        self.bimage = IMAGES['pipe'][1]
        self.brect = self.bimage.get_rect()
        self.brect.bottom = self.trect.top - random.choice(PIPE_GAPS)

    def update(self):
        self.trect.x += self.x_vel  # 管道x轴加移动速度
        if self.trect.x < 0:
            self.trect.top = random.randint(PIPE_HEIGHT_RANGE[0], PIPE_HEIGHT_RANGE[1])
            self.brect.bottom = self.trect.top - random.choice(PIPE_GAPS)
            self.trect.x = MAP_WIDTH

class Bird():
        def __init__(self, host):
            self.name = "NewBee"
            self.ip = host 
            self.frames = IMAGES['bird']  # 鸟儿框架
            self.frame_list = [0] * 5 + [1] * 5 + [2] * 5 + [1] * 5  # 控制小鸟翅膀运动上中下
            self.frame_index = 0
            self.image = self.frames[self.frame_list[self.frame_index]]  # 和菜单界面小鸟扇翅膀一个原理
            self.rect = self.image.get_rect()  # 鸟儿的矩形
            self.rect.x = MAP_WIDTH * 0.2
            self.rect.y = MAP_HEIGHT * 0.5 - IMAGES['bird'][0].get_height() / 2
            self.gravity = 1  # 重力
            self.flap_acc = -10  # 翅膀拍打往上飞 y坐标-10
            self.y_vel = -10  # y坐标的速度
            self.max_y_vel = 15  # y轴下落最大速度
            self.rotate = 0  # 脑袋朝向
            self.rotate_vel = -3  # 转向速度
            self.max_rotate = -30  # 最大转向速度
            self.flap_rotate = 45  # 按了空格只会脑袋朝向上30度
        def update(self, flap=False):
            if flap:
                self.y_vel = self.flap_acc  # 拍打翅膀 则y速度-10向上
                self.rotate = self.flap_rotate
            else:
                self.rotate = self.rotate + self.rotate_vel

            self.y_vel = min(self.y_vel + self.gravity, self.max_y_vel)
            self.rect.y += self.y_vel  # 小鸟向上移动的距离
            self.rorate = max(self.rotate + self.rotate_vel, self.max_rotate)

            self.frame_index += 1  # 扇翅膀的速率
            self.frame_index %= len(self.frame_list)  # 0~20
            self.image = self.frames[self.frame_list[self.frame_index]]
            self.image = pygame.transform.rotate(self.image, self.rotate)  # transform变形方法 旋转

        def go_die(self):
            if self.rect.y < FLOOR_H:
                self.y_vel = self.max_y_vel
                self.rect.y += self.y_vel
                self.rotate = -90
                self.image = self.frames[self.frame_list[self.frame_index]]
                self.image = pygame.transform.rotate(self.image, self.rotate)
#定义道具
class Prop:
    pass

class newMap():
    def __init__(self):
        self.Pipes = []
        self.Birds = []

class Data():
    def __init__(self):
        self.ip = 0
        self.up = 0
        self.prop = 0
        self.gameover = 0