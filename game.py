import single.py
import multi.py
import dress.py
import client
sound = 100
music = 100
dress = ['Default', 'Dynamic']
own_dress = 'Default'

#游戏界面
#包含 多人游戏，单人游戏，以及游戏设置
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
    single.main()

#多人模式
#详见Multi.py
def multi_type():
    client()

#设置
#详见setting.py
#界面有 设置皮肤 设置名字 调整声音大小 调整音效大小
def setting():
    pass
    setting.py()
    dress()


