import single.py
import multi.py
import dress.py

sound = 100
music = 100
dress = ['Default', 'Dynamic']

#��Ϸ����
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
def single_type():
    Single.game()

#����ģʽ
def multi_type():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = init_connection(sock)
    connecting(sock)

#����
def setting():
    setting.py()

#Ƥ��
def dress():
    
