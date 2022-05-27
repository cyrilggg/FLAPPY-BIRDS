# encoding=gbk
import pygame,random,sys,time
from pygame.locals import *#导入库文件
flappyBird = pygame.image.load("f:\project\FLAPPY-BIRDS\images\\bluebird-midflap.png")#加载游戏图片
level=1#游戏等级
 
class Brid:#鸟类
    position = [10,200]#初始位置
    speed=1#移动速度
    g_score = 0  # 游戏得分
    BridColor=pygame.Color(255,255,0)#颜色黄色
 
class PipeLine:#管道类
    pipe_x=300
    pipe_y=[]
    pipeColor=pygame.Color(115,190,44)
 
def GameOver():
    pygame.quit()#游戏退出
 
def Leveling(count):#等级判定
    if count<=10:
        return 1
    else:
        return count/10
 
def GameInit(windowSize,brid):#游戏初始化
    windowSize.blit(flappyBird,Rect(brid.position[0], brid.position[1], 30, 30))
    pygame.display.update()
 
def PipeInit(pipe):#初始化管道
    start = random.randint(0, 10) * 30
    pipe.pipe_y.append(start)
    pipe.pipe_y.append(start + 30)
    pipe.pipe_y.append(start + 60)
    pipe.pipe_y.append(start + 90)
 
def DrawPipeLine(windowSize,pipeList,bird):#绘制管道
    for pipe in pipeList:
        pipe.pipe_x=pipe.pipe_x - 10
        for i in range(0,20):
            if i*30 not in pipe.pipe_y:
                     pygame.draw.rect(windowSize, pygame.Color(0,145,0), Rect(pipe.pipe_x, i*30, 60, 30))
            if pipe.pipe_x<=-40:
                 bird.g_score = bird.g_score + 1
                 pipe.pipe_x=480
                 pipe.pipe_y=[]
                 PipeInit(pipe)
                 pipeList.pop()
                 pipeList.append(pipe)
 
 
def CheckGame(bird,pipe):#游戏判断
    if bird.position[1]<0 or bird.position[1]>570:
        pygame.quit()#跑出上下界限
    if bird.position[0]+30>pipe[0].pipe_x and bird.position[0]<pipe[0].pipe_x+60:
        if bird.position[1]<pipe[0].pipe_y[0] or bird.position[1]+20>pipe[0].pipe_y[3]:
            pygame.quit()#游戏退出
 
def main():
    flag=0#标记位
    pygame.init()#游戏初始化
    windowsSize=pygame.display.set_mode([480,600])#设置窗口大小
    pygame.display.set_caption('FlappyBrid')  # 窗口标题
    font = pygame.font.SysFont('宋体', 24)
    bird=Brid()#创建鸟实例
    pipeList=[]#管道列表
    pipe1= PipeLine()
    pipe2= PipeLine()
    PipeInit(pipe1)
    pipe2=pipe1#对象的值拷贝
    pipe2.pipe_x=pipe2.pipe_x+80
    pipeList.append(pipe1)
    pipeList.append(pipe2)
    windowsSize.fill(pygame.Color(113,197,205))
    GameInit(windowsSize,bird)#游戏初始化
    DrawPipeLine(windowsSize,pipeList,bird)
    while True:#游戏主体
        level = Leveling(bird.g_score)
        text = font.render("Game Score:" + str(bird.g_score), True, (255, 255, 255))
        text1 = font.render("Level:" + str(level), True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == QUIT:
                GameOver()  #游戏退出
            elif event.type==KEYDOWN:#按键响应
                if event.key==K_SPACE:
                    bird.position[1]=bird.position[1]-bird.speed*50*level
                    flag=1
        if flag==0:#检测位
            bird.position[1]=bird.position[1]+bird.speed*10*level
        flag=0
        windowsSize.fill(pygame.Color(113,197,205))
        CheckGame(bird, pipeList)
        DrawPipeLine(windowsSize,pipeList,bird)
        windowsSize.blit(text, Rect(360, 10, 200, 120))
        windowsSize.blit(text1, Rect(360, 40, 200, 120))
        GameInit(windowsSize,bird)
        time.sleep(0.1-level/100)
 
if __name__=='__main__':
    main()#主函数