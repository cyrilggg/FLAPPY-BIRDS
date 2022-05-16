import pygame,random,sys,time
level = 1

def GameOver():
    pygame.quit()#娓告垙閫€鍑�

def Leveling(count):#绛夌骇鍒ゅ畾
    if count<=10:
        return 1
    else:
        return count/10
 
def GameInit(windowsSize,bird):#娓告垙鍒濆鍖�
    pygame.draw.rect(windowsSize,bird.birdColor,Rect(bird.position[0],bird.position[1],30,30))
    pygame.display.update()

class Bird:#鑳栭笩绫�
    position=[30,200]#楦熺殑鍒濆浣嶇疆
    birdColor=pygame.Color(255,255,0)#涓€鍙粍鑹茬殑灏忛笩
    speed=1#灏忛笩鐨勯€熷害
    bird_score=0#灏忛笩寰楀垎

class PipeLine:#绠￠亾绫�
    pipe_x=300#璁板綍绠￠亾妯潗鏍囦綅缃�
    pipe_y=[]#鐣欑粰灏忛笩椋炶鐨勯棿闅�
    pipeColor=pygame.Color(115,190,44)#绠￠亾鐨勯鑹�

def PipeInit(pipe):#鍒濆鍖栫閬�
    start = random.randint(0, 10) * 30
    pipe.pipe_y.append(start)
    pipe.pipe_y.append(start + 30)
    pipe.pipe_y.append(start + 60)
    pipe.pipe_y.append(start + 90)

def DrawPipeLine(windowSize,pipeList,bird):#缁樺埗绠￠亾
    for pipe in pipeList:
        pipe.pipe_x=pipe.pipe_x - 10
        for i in range(0,20):
            if i*30 not in pipe.pipe_y:#not in瀹炵幇绌洪殭鐨勭暀鐧�
                     pygame.draw.rect(windowSize, pygame.Color(0,145,0), Rect(pipe.pipe_x, i*30, 60, 30))#缁樺埗鐭╁舰绠￠亾
            if pipe.pipe_x<=-40:#鍒ゆ柇绠￠亾鏄惁绉诲姩鍑虹晫
                 bird.bird_score = bird.bird_score + 1#娓告垙鎴愮哗澧炲姞
                 pipe.pipe_x=480
                 pipe.pipe_y=[]
                 PipeInit(pipe)
                 pipeList.pop()#寮瑰嚭绉诲嚭灞忓箷鐨勭閬�
                 pipeList.append(pipe)#灏嗘柊绠￠亾娣诲姞杩涘叆绠￠亾鍒楄〃

def CheckGame(bird,pipe):#娓告垙鍒ゆ柇
    if bird.position[1]<0 or bird.position[1]>570:
        pygame.quit()#璺戝嚭涓婁笅鐣岄檺
    if bird.position[0]+30>pipe[0].pipe_x and bird.position[0]<pipe[0].pipe_x+60:
        if bird.position[1]<pipe[0].pipe_y[0] or bird.position[1]+20>pipe[0].pipe_y[3]:
            pygame.quit()#娓告垙閫€鍑�

def DrawRect(windowsSize,bird):
    pygame.draw.rect(windowsSize,bird.birdColor,Rect(bird.position[0],bird.position[1],30,30))

def game():
    flag=0#鏍囪浣�
    pygame.init()#娓告垙鍒濆鍖�
    windowsSize=pygame.display.set_mode([480,600])#璁剧疆绐楀彛澶у皬
    pygame.display.set_caption('FlappyBrid')  # 绐楀彛鏍囬
    font = pygame.font.SysFont('瀹嬩綋', 24)
    bird=Bird()#鍒涘缓楦熷疄渚�
    pipeList=[]#绠￠亾鍒楄〃
    pipe1= PipeLine()
    pipe2= PipeLine()
    PipeInit(pipe1)
    pipe2=pipe1#瀵硅薄鐨勫€兼嫹璐�
    pipe2.pipe_x=pipe2.pipe_x+80
    pipeList.append(pipe1)
    pipeList.append(pipe2)
    windowsSize.fill(pygame.Color(113,197,205))
    GameInit(windowsSize,bird)#娓告垙鍒濆鍖�
    DrawPipeLine(windowsSize,pipeList,bird)
    while True:#娓告垙涓讳綋
        level = Leveling(bird.bird_score)
        text = font.render("Game Score:" + str(bird.bird_score), True, (255, 255, 255))
        text1 = font.render("Level:" + str(level), True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == QUIT:
                GameOver()  #娓告垙閫€鍑�
            elif event.type==KEYDOWN:#鎸夐敭鍝嶅簲
                if event.key==K_SPACE:
                    bird.position[1]=bird.position[1]-bird.speed*50*level
                    flag=1
        if flag==0:#妫€娴嬩綅
            bird.position[1]=bird.position[1]+bird.speed*10*level
        flag=0
        windowsSize.fill(pygame.Color(113,197,205))
        CheckGame(bird, pipeList)
        DrawPipeLine(windowsSize,pipeList,bird)
        windowsSize.blit(text, Rect(360, 10, 200, 120))
        windowsSize.blit(text1, Rect(360, 40, 200, 120))
        GameInit(windowsSize,bird)
        time.sleep(0.1-level/100)

