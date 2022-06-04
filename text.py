# encoding=gbk
import pygame
import time
 
class TextBox:
    def __init__(self, w, h, x, y, font=None):
        """
        :param w:文本框宽度
        :param h:文本框高度
        :param x:文本框坐标
        :param y:文本框坐标
        :param font:文本框中使用的字体
        """
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.text = ""  # 文本框内容
        # 创建
        self.__surface = pygame.Surface((w, h))
        self.__surface.fill((47,79,79))
        
        if font is None:
            self.font = pygame.font.Font(None, 32)  # 使用pygame自带字体
        else:
            self.font = font
 
    def draw(self, dest_surf, str):
        
        dest_surf.blit(self.__surface, (self.x, self.y))

        str_image = self.font.render(str, True, (255, 255, 255))
        str_rect = str_image.get_rect()
        str_rect.center = ((self.x + self.width / 2), ((self.y + self.height / 2) - 30))
        dest_surf.blit(str_image, str_rect)

        msg_image = self.font.render(self.text, True, (255, 255, 255))
        msg_rect = msg_image.get_rect()
        msg_rect.center = ((self.x + self.width / 2), ((self.y + self.height / 2)))
    
        dest_surf.blit(msg_image, msg_rect)

    def key_down(self, event):
        unicode = event.unicode
        key = event.key
 
        # 退位键
        if key == 8:
            self.text = self.text[:-1]
            return
 
        # 切换大小写键
        if key == 301:
            return
 
        # 回车键
        if key == 13:
            if self.callback is not None:
                self.callback()
            return
 
        if unicode != "":
            char = unicode
        else:
            char = chr(key)
 
        self.text += char

def get_text(winSur, str):
    text_box = TextBox(180, 30, 55, 200)
    # 游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == 13:
                    time.sleep(0.3)
                    return text_box.text
                else:
                    text_box.key_down(event)
        #pygame.time.delay(33)
        text_box.draw(winSur, str)
        pygame.display.flip()

def main():
    pygame.init()
    winSur = pygame.display.set_mode((640, 480))
    # 创建文本框
    msg = get_text(winSur)
    print(msg)
 
if __name__ == '__main__':
    main()