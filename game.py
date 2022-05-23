import single.py
import multi.py
import dress.py

sound = 100
music = 100
dress = ['Default', 'Dynamic']
own_dress = 'Default'

#游戏界面
#包含 多人游戏，单人游戏，以及皮肤和游戏设置
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

#单人模式
#通过上次写的代码直接借鉴即可
def single_type():
    Single.game()

#多人模式
#详见Multi.py
def multi_type():
    global own_dress
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = init_connection(sock)
    connecting(sock)
    Multi.game(own_dress)

#设置
#详见setting.py
#界面有 设置皮肤 设置名字 调整声音大小 调整音效大小
def setting():
    setting.py()
    dress()

#皮肤
#界面：各个皮肤的描述和样子 点击选择，选择后更新全局变量，即皮肤的信息
#游戏时实时更新皮肤
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


