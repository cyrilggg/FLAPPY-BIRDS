# encoding=gbk
import pygame,random,sys,time
from pygame.locals import *#������ļ�
flappyBird = pygame.image.load("f:\project\FLAPPY-BIRDS\images\\bluebird-midflap.png")#������ϷͼƬ
level=1#��Ϸ�ȼ�
 
class Brid:#����
    position = [10,200]#��ʼλ��
    speed=1#�ƶ��ٶ�
    g_score = 0  # ��Ϸ�÷�
    BridColor=pygame.Color(255,255,0)#��ɫ��ɫ
 
class PipeLine:#�ܵ���
    pipe_x=300
    pipe_y=[]
    pipeColor=pygame.Color(115,190,44)
 
def GameOver():
    pygame.quit()#��Ϸ�˳�
 
def Leveling(count):#�ȼ��ж�
    if count<=10:
        return 1
    else:
        return count/10
 
def GameInit(windowSize,brid):#��Ϸ��ʼ��
    windowSize.blit(flappyBird,Rect(brid.position[0], brid.position[1], 30, 30))
    pygame.display.update()
 
def PipeInit(pipe):#��ʼ���ܵ�
    start = random.randint(0, 10) * 30
    pipe.pipe_y.append(start)
    pipe.pipe_y.append(start + 30)
    pipe.pipe_y.append(start + 60)
    pipe.pipe_y.append(start + 90)
 
def DrawPipeLine(windowSize,pipeList,bird):#���ƹܵ�
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
 
 
def CheckGame(bird,pipe):#��Ϸ�ж�
    if bird.position[1]<0 or bird.position[1]>570:
        pygame.quit()#�ܳ����½���
    if bird.position[0]+30>pipe[0].pipe_x and bird.position[0]<pipe[0].pipe_x+60:
        if bird.position[1]<pipe[0].pipe_y[0] or bird.position[1]+20>pipe[0].pipe_y[3]:
            pygame.quit()#��Ϸ�˳�
 
def main():
    flag=0#���λ
    pygame.init()#��Ϸ��ʼ��
    windowsSize=pygame.display.set_mode([480,600])#���ô��ڴ�С
    pygame.display.set_caption('FlappyBrid')  # ���ڱ���
    font = pygame.font.SysFont('����', 24)
    bird=Brid()#������ʵ��
    pipeList=[]#�ܵ��б�
    pipe1= PipeLine()
    pipe2= PipeLine()
    PipeInit(pipe1)
    pipe2=pipe1#�����ֵ����
    pipe2.pipe_x=pipe2.pipe_x+80
    pipeList.append(pipe1)
    pipeList.append(pipe2)
    windowsSize.fill(pygame.Color(113,197,205))
    GameInit(windowsSize,bird)#��Ϸ��ʼ��
    DrawPipeLine(windowsSize,pipeList,bird)
    while True:#��Ϸ����
        level = Leveling(bird.g_score)
        text = font.render("Game Score:" + str(bird.g_score), True, (255, 255, 255))
        text1 = font.render("Level:" + str(level), True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == QUIT:
                GameOver()  #��Ϸ�˳�
            elif event.type==KEYDOWN:#������Ӧ
                if event.key==K_SPACE:
                    bird.position[1]=bird.position[1]-bird.speed*50*level
                    flag=1
        if flag==0:#���λ
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
    main()#������