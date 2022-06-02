# encoding=gbk
# ��ť�Ļ��࣬���ǿ���ͨ��ʵ������ť�����������ְ�ť
import pygame
class Button():
    # ��ʼ����ť
    def __init__(self, screen, settings, msg, width, height):
        
        self.screen = screen
        self.settings = settings
        # ���ð�ť�ĳߴ�
        self.width = 100
        self.height = 50
        # ���ð�ť����ɫ
        self.button_color = (78,238,148)
        # �����ı�����ɫ
        self.text_color = (255, 255, 255)
        # �����ı�������
        self.font = pygame.font.Font(None, 32)
        # ���ð�ť��λ��
        self.rect = pygame.Rect(width, height, self.width, self.height)
        # ���ı���Ⱦ�� Surface����
        self.prep_msg(msg)
        
        self.image = pygame.image.load('.\images\\' + 'return.png')
        self.image_rect = self.image.get_rect()
        self.image_rect.x = width
        self.image_rect.y = height

    def prep_msg(self, msg):
        # ���ı��ַ�����Ⱦ��һ��Surface����
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        # ��ȡ�ı�������
        self.msg_rect = self.msg_image.get_rect()
        # ���ı�λ�÷ŵ���ť�м�
        self.msg_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_rect)
    
    def draw_image(self):
        self.screen.blit(self.image, self.image_rect)

