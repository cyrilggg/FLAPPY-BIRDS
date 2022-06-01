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

#接收地图数据并回传
def threaded_client(conn, addr):
    global Map
    conn.send(addr[0].encode()) #回传自己的ip
    #send_to_all_client()
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            print(type(data),data.up)
            
            if not data:
                print("Disconnected")
                break
            else:
                #更新数据
                analize_map(data)
                print("Received: ", data)
                print("Sending : ", Map)
            
            send_to_all_client()
            time.sleep(0.03)
        except Exception as e:
            import traceback
            traceback.print_exc()
            break


    print("Lost connection")

#更新地图
def analize_map(Data):
    
    global Map
    for pipe in Map.Pipes:
        pipe.update()
    #if Data.gameover:
        #return
    
    for bird in Map.Birds:
        if bird.gameover == 1:
            if bird.rect.y < FLOOR_H:
                bird.update(False)
            if bird.rect.x > -50:
                bird.rect.x -= 5
            continue
        
        if bird.ip == Data.ip:
            #使用道具
            flap = False
            if Data.prop:
                pass
            if Data.up:
                flap = True
            bird.update(flap)
            if  bird.rect.y > FLOOR_H or bird.rect.y < 0:
                # 保存死亡时的鸟儿 分数 管道 继续显示在结束窗口
                bird.gameover = 1
                bird.go_die()
            for pipe in Map.Pipes:
                if pipe.trect.colliderect(bird.rect) or pipe.brect.colliderect(bird.rect):
                    bird.gameover = 1
                    bird.go_die() 
            #当小鸟左边大于 管道右边就得分
            if min(Map.Pipes[0].trect.x, Map.Pipes[1].trect.x) == 56:
                bird.score += 1
     
#碰撞了就删掉
    
#设置服务器

#线程：一直更新柱子
def update_pipe():
    global Map
    while True:
        for pipe in Map.Pipes:
            pipe.update()

def init():
    global HOST, PORT, ADDR
    HOST = input("Please input host ip:")
    PORT = 5555
    ADDR = (HOST, PORT)


def Game_Start(conn, addr):
    global Map
    #start_new_thread(update_pipe,())#开一个线程去全局更新地图
    bird = Bird(addr[0])
    Map.Birds.append(bird)
    start_new_thread(threaded_client, (conn, addr))
    #start_new_thread(send_to_all_client, ())    

def main():
    global currentplayer, Map, conns
    currentplayer = 0
    Map = newMap()
    conns = []
    
    Pipe1 = Pipe(MAP_WIDTH)
    Pipe2 = Pipe(MAP_WIDTH + PIPE_DISTANCE)
    Map.Pipes.append(Pipe1)
    Map.Pipes.append(Pipe2)
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(ADDR)
            print('[*] Server started at: ', ADDR)
            #最多给5个人同时玩，避免服务器崩了
            s.listen(MAX_LISTEN)
            currentPlayer = 0
            while True:
                # 等待客户端连接请求]
                conn, addr = s.accept()
                conns.append(conn)
                print('[*] Client connected from: ',addr[0],':',addr[1],sep='')
                Game_Start(conn, addr)
            print("current game is over")
            s.close()

init()
if __name__ == '__main__':
    main() 