# encoding=gbk
import pygame
 
 
class TextBox:
    def __init__(self, w, h, x, y, font=None, callback=None):
        """
        :param w:�ı�����
        :param h:�ı���߶�
        :param x:�ı�������
        :param y:�ı�������
        :param font:�ı�����ʹ�õ�����
        :param callback:���ı����»س���֮��Ļص�����
        """
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.text = ""  # �ı�������
        self.callback = callback
        # ����
        self.__surface = pygame.Surface((w, h))
        # ���fontΪNone,��ôЧ�����ܲ�̫�ã����鴫��font�����õ���
        if font is None:
            self.font = pygame.font.Font(None, 32)  # ʹ��pygame�Դ�����
        else:
            self.font = font
 
    def draw(self, dest_surf):
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        dest_surf.blit(self.__surface, (self.x, self.y))
        dest_surf.blit(text_surf, (self.x, self.y + (self.height - text_surf.get_height())),
                       (0, 0, self.width, self.height))
 
    def key_down(self, event):
        unicode = event.unicode
        key = event.key
 
        # ��λ��
        if key == 8:
            self.text = self.text[:-1]
            return
 
        # �л���Сд��
        if key == 301:
            return
 
        # �س���
        if key == 13:
            if self.callback is not None:
                print(self.text)
                self.callback()
            return
 
        if unicode != "":
            char = unicode
        else:
            char = chr(key)
 
        self.text += char
 
 
def callback():
    print("�س�����")
 
 
def main():
    # Ӣ���ı���demo
    pygame.init()
    winSur = pygame.display.set_mode((640, 480))
    # �����ı���
    text_box = TextBox(200, 30, 200, 200, callback=callback)
 
    # ��Ϸ��ѭ��
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                text_box.key_down(event)
        pygame.time.delay(33)
        winSur.fill((0, 50, 0))
        text_box.draw(winSur)
        pygame.display.flip()
 
 
if __name__ == '__main__':
    main()