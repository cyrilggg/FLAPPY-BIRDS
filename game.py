import single.py
import multi.py
import dress.py

sound = 100
music = 100
dress = ['Default', 'Dynamic']
own_dress = 'Default'

#��Ϸ����
#���� ������Ϸ��������Ϸ���Լ�Ƥ������Ϸ����
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
    Single.game()

#����ģʽ
#���Multi.py
def multi_type():
    global own_dress
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = init_connection(sock)
    connecting(sock)
    Multi.game(own_dress)

#����
#���setting.py
#������ ����Ƥ�� �������� ����������С ������Ч��С
def setting():
    setting.py()
    dress()

#Ƥ��
#���棺����Ƥ�������������� ���ѡ��ѡ������ȫ�ֱ�������Ƥ������Ϣ
#��Ϸʱʵʱ����Ƥ��
def dress():
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


