import single.py
import multi.py
import dress.py
import client
sound = 100
music = 100
dress = ['Default', 'Dynamic']
own_dress = 'Default'

#��Ϸ����
#���� ������Ϸ��������Ϸ���Լ���Ϸ����
def main_title():
    while(True):
        for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("[KEYDOWN]:", "#",event.key,event.mod)
            else:
                print("[KEYDOWN]:",event.unicode,event.key,event.mod)
        elif event.type == pygame.MOUSEMOTION:
            print("[MOUSEMOTION]:",event.pos,event.rel,event.buttons)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("[MOUSEBUTTONDOWN]:",event.pos,event.button)
        elif event.type == pygame.MOUSEBUTTONUP:
            print("[MOUSEBUTTONUP]:",event.pos,event.button)

    pygame.display.update()

#����ģʽ
#ͨ���ϴ�д�Ĵ���ֱ�ӽ������
def single_type():
    single.main()

#����ģʽ
#���Multi.py
def multi_type():
    client()

#����
#���setting.py
#������ ����Ƥ�� �������� ����������С ������Ч��С
def setting():
    pass
    setting.py()
    dress()


