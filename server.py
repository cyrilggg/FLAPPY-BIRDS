# encoding=gbk
import socket
import pickle
from _thread import *
from Map_Data import *
import time

HOST = '192.168.1.32'
PORT = 5555
ADDR = (HOST, PORT)
BUFFSIZE = 1024
MAX_LISTEN = 5

currentplayer = 0
Map = newMap()
conns = []

number_of_clients = 0

ready_players = 0
dead_players=0

UPDATE = 0

GameState = "Gameover"
ready = []

def send_to_all_client():
    global Map
    for conn in conns:
        try:
            conn.sendall(pickle.dumps(Map))
        except socket.error as e:
            print("发送失败")
            print(conn)
            print(e)
            return

def handle_disconnect(conn, addr):
    #Removes player from the lists
    global Map, number_of_clients,conns, GameState, ready_players, dead_players
    Birdss = []
    ncons = []
    for bird in Map.Birds:
        if bird.ip != addr[0]:
            Birdss.append(bird)
        else:
            if bird.curstate:
                ready_players -= 1
            if bird.surstate:
                dead_players -= 1

    for co in conns:
        if co != conn:
            ncons.append(co)

    conns = ncons
    Map.Birds = Birdss   
    #Map.Birds.pop(client)
    #conns.pop(client)
    number_of_clients -= 1
    if number_of_clients == 0:
        Pipe_Init()
        GameState = "Gameover"

#接收地图数据并回传
def threaded_client(conn, addr):
    global Map, number_of_clients, ready_players, dead_players, GameState
    number_of_clients += 1
    curstate = False
    surstate = False
    global SCORE_UPDATE
    while True:
        try:
            #print(ready)
            data = pickle.loads(conn.recv(2048))
            #print(type(data),data.up)
            flag = True
            if not data:
                print("Disconnected")
                break
            else:
                #游戏开始
                for bird in Map.Birds:
                    if bird.ip == addr[0]:
                        if data.up and not bird.curstate:
                            bird.ready = 1
                            bird.curstate = True
                            ready_players += 1
                            ready.append(addr[0])
                        print(GameState, ready_players, number_of_clients)
                        if GameState == "Gameover" and ready_players >= number_of_clients:
                            print("GAMESTART")
                            for bird in Map.Birds:
                                bird.gamestate2 = 1
                            flag = False
                            send_to_all_client()
                            #conn.sendall(pickle.dumps(Map))
                            for bird in Map.Birds:
                                bird.gamestate2 = 0
                            GameState = "Start"
                            ready_players = 0
                            time.sleep(2)
                            SCORE_UPDATE = 0
                            start_new_thread(update_pipe,())#开一个线程去全局更新地图
                                
                        
                        if data.gameover and not bird.surstate:
                            bird.surstate = True
                            dead_players += 1
                        if GameState == "Start" and dead_players >= number_of_clients:
                            for bird in Map.Birds:
                                bird.gamestate1 = 1
                                bird.curstate = False
                                bird.surstate = False
                            flag = False
                            send_to_all_client()
                            #conn.sendall(pickle.dumps(Map))
                            GameState = "Gameover"
                            Pipe_Init()
                            for bird in Map.Birds:
                                bird.__init__(bird.ip, bird.name)
                            bird.curstate = False
                            bird.surstate = False
                            dead_players = 0
                            ready.clear()
                
                #更新数据
                if GameState == "Start":
                    analize_map(data)
            
            if flag:
                #send_to_all_client()
                conn.sendall(pickle.dumps(Map))
            time.sleep(0.1)
        except Exception as e:
            import traceback
            traceback.print_exc()
            print('[!] Client disconnected!')
            handle_disconnect(conn, addr)
            break


    print("Lost connection")

#更新地图
def analize_map(Data):
    
    global Map, UPDATE
    #for pipe in Map.Pipes:
    #    pipe.update()
    #print(Data.ip, Map.Birds[0].ip)
    for bird in Map.Birds:
        if bird.gameover == 1:
            if bird.rect.y < FLOOR_H:
                bird.update(False)
            if bird.rect.x > -50:
                bird.rect.x -= 5
            continue
        
        if bird.ip == Data.ip:
            #print (bird.ip, Data.ip)
            #使用道具
            flap = False
            if Data.prop:
                bird.invincibility_time = 100
            if Data.up:
                flap = True
            bird.update(flap)
            if not bird.invincibility_time:
                if  bird.rect.y > FLOOR_H or bird.rect.y < 0:
                    # 保存死亡时的鸟儿 分数 管道 继续显示在结束窗口
                    bird.gameover = 1
                    bird.go_die()
                for pipe in Map.Pipes:
                    if pipe.trect.colliderect(bird.rect) or pipe.brect.colliderect(bird.rect):
                        bird.gameover = 1
                        bird.go_die() 
        #当小鸟左边大于 管道右边就得分
            #if (Map.Pipes[0].trect.x <= 56 and Map.Pipes[0].trect.x >= 53) or (Map.Pipes[1].trect.x <= 56 and Map.Pipes[1].trect.x >= 53) == 56:
                #bird.score += 1
    if UPDATE == 1:
        for bird in Map.Birds:
            bird.score += 1
        UPDATE = 0
    
#碰撞了就删掉
#设置服务器 

#线程：一直更新柱子
def update_pipe():
    global Map, UPDATE
    while GameState == "Start":
        for pipe in Map.Pipes:
            if (pipe.update()):
                UPDATE = 1

        time.sleep(0.06)

def init():
    global HOST, PORT, ADDR
    HOST = input("Please input host ip:")
    PORT = 5555
    ADDR = (HOST, PORT)


def Game_Start(conn, addr):
    global urrentplayer, Map, conns, number_of_clients
    #start_new_thread(update_pipe,())#开一个线程去全局更新地图
    name = conn.recv(1024).decode()
    print('[*] Recieved name from client',name)
    bird = Bird(addr[0], name)
    Map.Birds.append(bird)
    conn.send(addr[0].encode()) #回传自己的ip
    start_new_thread(threaded_client, (conn, addr))

def Pipe_Init():
    global Map, SCORE_UPDATE
    SCORE_UPDATE = 0
    Map.Pipes.clear()
    Pipe1 = Pipe(MAP_WIDTH)
    Pipe2 = Pipe(MAP_WIDTH + 160)
    Map.Pipes.append(Pipe1)
    Map.Pipes.append(Pipe2)

def main():
    global currentplayer, Map, conns, number_of_clients
    Map = newMap()
    conns = []
    Pipe_Init()
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(ADDR)
            print('[*] Server started at: ', ADDR)
            #最多给5个人同时玩，避免服务器崩了
            s.listen(MAX_LISTEN)
            currentPlayer = 0
            while True:
                # 等待客户端连接请求
                conn, addr = s.accept()
                conns.append(conn)
                print('[*] Client connected from: ',addr[0],':',addr[1],sep='')
                Game_Start(conn, addr) #给他单独开一个开始游戏的线程
            print("current game is over")
            s.close()

init()
if __name__ == '__main__':
    main() 