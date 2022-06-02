# encoding=gbk
# 按钮的基类，我们可以通过实例化按钮类来创建各种按钮
import pygame
class Button():
    # 初始化按钮
    def __init__(self, screen, settings, msg, width, height):
        
        self.screen = screen
        self.settings = settings
        # 设置按钮的尺寸
        self.width = 100
        self.height = 50
        # 设置按钮的颜色
        self.button_color = (78,238,148)
        # 设置文本的颜色
        self.text_color = (255, 255, 255)
        # 设置文本的字体
        self.font = pygame.font.Font(None, 32)
        # 设置按钮的位置
        self.rect = pygame.Rect(width, height, self.width, self.height)
        # 将文本渲染成 Surface对象
        self.prep_msg(msg)
        
        self.image = pygame.image.load('.\images\\' + 'return.png')
        self.image_rect = self.image.get_rect()
        self.image_rect.x = width
        self.image_rect.y = height

    def prep_msg(self, msg):
        # 将文本字符串渲染成一个Surface对象
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        # 获取文本的坐标
        self.msg_rect = self.msg_image.get_rect()
        # 将文本位置放到按钮中间
        self.msg_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_rect)
    
    def draw_image(self):
        self.screen.blit(self.image, self.image_rect)

