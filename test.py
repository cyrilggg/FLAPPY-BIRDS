#coding: gbk
from calendar import c
import os
import random
import sys
 
import pygame
from pygame import font
from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION
 
 
class Color:
    # �Զ�����ɫ
    ACHIEVEMENT = (220, 160, 87)
    VERSION = (220, 160, 87)
 
    # �̶���ɫ
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)  # ���Ի�
    TRANSPARENT = (255, 255, 255, 0)  # ��ɫ����ȫ͸��
 
 
class Text:
    def __init__(self, text: str, text_color: Color, font_type: str, font_size: int):
        """
        text: �ı����ݣ���'��ѧ��ģ����'��ע�����ַ�����ʽ
        text_color: ������ɫ����Color.WHITE��COLOR.BLACK
        font_type: �����ļ�(.ttc)����'msyh.ttc'��ע�����ַ�����ʽ
        font_size: �����С����20��10
        """
        self.text = text
        self.text_color = text_color
        self.font_type = font_type
        self.font_size = font_size
 
        font = pygame.font.Font(os.path.join('font', (self.font_type)), self.font_size)
        self.text_image = font.render(self.text, True, self.text_color).convert_alpha()
 
        self.text_width = self.text_image.get_width()
        self.text_height = self.text_image.get_height()
 
    def draw(self, surface: pygame.Surface, center_x, center_y):
        """
        surface: �ı����õı���
        center_x, center_y: �ı������ڱ����<��������>
        """
        upperleft_x = center_x - self.text_width / 2
        upperleft_y = center_y - self.text_height / 2
        surface.blit(self.text_image, (upperleft_x, upperleft_y))
 
 
class Image:
    def __init__(self, img_name: str, ratio=0.4):
        """
        img_name: ͼƬ�ļ�������'background.jpg'��'ink.png',ע��Ϊ�ַ���
        ratio: ͼƬ���ű�����������Ļ����Ӧ��Ĭ��ֵΪ0.4
        """
        self.img_name = img_name
        self.ratio = ratio
 
        self.image_1080x1920 = pygame.image.load(os.path.join('image', self.img_name)).convert_alpha()
        self.img_width = self.image_1080x1920.get_width()
        self.img_height = self.image_1080x1920.get_height()
 
        self.size_scaled = self.img_width * self.ratio, self.img_height * self.ratio
 
        self.image_scaled = pygame.transform.smoothscale(self.image_1080x1920, self.size_scaled)
        self.img_width_scaled = self.image_scaled.get_width()
        self.img_height_scaled = self.image_scaled.get_height()
 
    def draw(self, surface: pygame.Surface, center_x, center_y):
        """
        surface: ͼƬ���õı���
        center_x, center_y: ͼƬ�����ڱ����<��������>
        """
        upperleft_x = center_x - self.img_width_scaled / 2
        upperleft_y = center_y - self.img_height_scaled / 2
        surface.blit(self.image_scaled, (upperleft_x, upperleft_y))
 
 
class ColorSurface:
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height
 
        self.color_image = pygame.Surface((self.width, self.height)).convert_alpha()
        self.color_image.fill(self.color)
 
    def draw(self, surface: pygame.Surface, center_x, center_y):
        upperleft_x = center_x - self.width / 2
        upperleft_y = center_y - self.height / 2
        surface.blit(self.color_image, (upperleft_x, upperleft_y))
 
 
class ButtonText(Text):
    def __init__(self, text: str, text_color: Color, font_type: str, font_size: int):
        super().__init__(text, text_color, font_type, font_size)
        self.rect = self.text_image.get_rect()
 
    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y
 
    def handle_event(self, command):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            command()
 
 
class ButtonImage(Image):
    def __init__(self, img_name: str, ratio=0.4):
        super().__init__(img_name, ratio)
        self.rect = self.image_scaled.get_rect()
 
    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y
 
    def handle_event(self, command):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            command()
 
 
class ButtonColorSurface(ColorSurface):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
        self.rect = self.color_image.get_rect()
 
    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y
 
    def handle_event(self, command, *args):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            command(*args)