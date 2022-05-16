import pygame,random,sys,time
level = 1

def GameOver():
    pygame.quit()#游戏逢�凄1�7

def Leveling(count):#等级判定
    if count<=10:
        return 1
    else:
        return count/10
 
def GameInit(windowsSize,bird):#游戏初始匄1�7
    pygame.draw.rect(windowsSize,bird.birdColor,Rect(bird.position[0],bird.position[1],30,30))
    pygame.display.update()

class Bird:#胖鸟籄1�7
    position=[30,200]#鸟的初始位置
    birdColor=pygame.Color(255,255,0)#丢�只黄色的小鸟
    speed=1#小鸟的��度
    bird_score=0#小鸟得分

class PipeLine:#管道籄1�7
    pipe_x=300#记录管道横坐标位罄1�7
    pipe_y=[]#留给小鸟飞行的间隄1�7
    pipeColor=pygame.Color(115,190,44)#管道的颜艄1�7

def PipeInit(pipe):#初始化管遄1�7
    start = random.randint(0, 10) * 30
    pipe.pipe_y.append(start)
    pipe.pipe_y.append(start + 30)
    pipe.pipe_y.append(start + 60)
    pipe.pipe_y.append(start + 90)

def DrawPipeLine(windowSize,pipeList,bird):#绘制管道
    for pipe in pipeList:
        pipe.pipe_x=pipe.pipe_x - 10
        for i in range(0,20):
            if i*30 not in pipe.pipe_y:#not in实现空隙的留癄1�7
                     pygame.draw.rect(windowSize, pygame.Color(0,145,0), Rect(pipe.pipe_x, i*30, 60, 30))#绘制矩形管道
            if pipe.pipe_x<=-40:#判断管道是否移动出界
                 bird.bird_score = bird.bird_score + 1#游戏成绩增加
                 pipe.pipe_x=480
                 pipe.pipe_y=[]
                 PipeInit(pipe)
                 pipeList.pop()#弹出移出屏幕的管遄1�7
                 pipeList.append(pipe)#将新管道添加进入管道列表

def CheckGame(bird,pipe):#游戏判断
    if bird.position[1]<0 or bird.position[1]>570:
        pygame.quit()#跑出上下界限
    if bird.position[0]+30>pipe[0].pipe_x and bird.position[0]<pipe[0].pipe_x+60:
        if bird.position[1]<pipe[0].pipe_y[0] or bird.position[1]+20>pipe[0].pipe_y[3]:
            pygame.quit()#游戏逢�凄1�7

def DrawRect(windowsSize,bird):
    pygame.draw.rect(windowsSize,bird.birdColor,Rect(bird.position[0],bird.position[1],30,30))

def game():
    flag=0#标记佄1�7
    pygame.init()#游戏初始匄1�7
    windowsSize=pygame.display.set_mode([480,600])#设置窗口大小
    pygame.display.set_caption('FlappyBrid')  # 窗口标题
    font = pygame.font.SysFont('宋体', 24)
    bird=Bird()#创建鸟实侄1�7
    pipeList=[]#管道列表
    pipe1= PipeLine()
    pipe2= PipeLine()
    PipeInit(pipe1)
    pipe2=pipe1#对象的��拷贄1�7
    pipe2.pipe_x=pipe2.pipe_x+80
    pipeList.append(pipe1)
    pipeList.append(pipe2)
    windowsSize.fill(pygame.Color(113,197,205))
    GameInit(windowsSize,bird)#游戏初始匄1�7
    DrawPipeLine(windowsSize,pipeList,bird)
    while True:#游戏主体
        level = Leveling(bird.bird_score)
        text = font.render("Game Score:" + str(bird.bird_score), True, (255, 255, 255))
        text1 = font.render("Level:" + str(level), True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == QUIT:
                GameOver()  #游戏逢�凄1�7
            elif event.type==KEYDOWN:#按键响应
                if event.key==K_SPACE:
                    bird.position[1]=bird.position[1]-bird.speed*50*level
                    flag=1
        if flag==0:#棢�测位
            bird.position[1]=bird.position[1]+bird.speed*10*level
        flag=0
        windowsSize.fill(pygame.Color(113,197,205))
        CheckGame(bird, pipeList)
        DrawPipeLine(windowsSize,pipeList,bird)
        windowsSize.blit(text, Rect(360, 10, 200, 120))
        windowsSize.blit(text1, Rect(360, 40, 200, 120))
        GameInit(windowsSize,bird)
        time.sleep(0.1-level/100)

