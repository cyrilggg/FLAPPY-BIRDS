# encoding=gbk
import socket
import pickle
from _thread import *
from Map_Data import *
import time

HOST = '127.0.0.1'
PORT = 5555
ADDR = (HOST, PORT)
BUFFSIZE = 1024
MAX_LISTEN = 2
    
Map = newMap()

#更新地图
def analize_map(Data):
    global Map
    if Data.Gameover:
        return
    #使用道具
    if Data.Prop:
        pass
    
    if Data.up:
        flap = True
    for bird in Map.Birds:
        if bird.gameover == 1:
            continue
        if bird.ip == Data.ip:
            bird.update(flap)
        if  bird.rect.y > FLOOR_H or bird.rect.y < 0:
            # 保存死亡时的鸟儿 分数 管道 继续显示在结束窗口
            bird.gameover = 1
        
        #当小鸟左边大于 管道右边就得分
        if min(Map.Pipes[0].trect.x, Map.Pipes[1].trect.x) < bird.rect.x:
            bird.score += 1
     
    #碰撞了就删掉
    
#设置服务器

#线程：一直更新柱子
def update_pipe():
    global Map
    while True:
        for pipes in Map.Pipes:
            pipes.update()

def init():
    global HOST, PORT, ADDR, Map
    HOST = '127.0.0.1'
    PORT = 5555
    ADDR = (HOST, PORT)

    Pipe1 = Pipe(MAP_WIDTH)
    Pipe2 = Pipe(MAP_WIDTH + PIPE_DISTANCE)
    Map.Pipes.append(Pipe1)
    Map.Pipes.append(Pipe2)

def Game_Start(conn, addr):
    global Map
    start_new_thread(update_pipe,())#开一个线程去全局更新地图
    index = 0
    bird = Bird(addr)
    Map.Birds.append(bird)
    conn.sendall(pickle.dumps(Map))
    while True:
        try:
            print("Trying")
            data = pickle.loads(conn.recv(2048))
            #print(type(data), data.ip, data.up, data.prop,data.gameover)
            if not data:
                print("Disconnected")
                break
            else:
                #更新数据
                analize_map(data)
                print("Received: ", data)
                print("Sending : ", Map)

            conn.sendall(pickle.dumps(Map))
        except:
            break

    print("Lost connection")
    conn.close()
    
def main():
    init()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 绑定服务器地址和端口
        s.bind(ADDR)
        # 启动服务监听
        s.listen(MAX_LISTEN)
        print('Wating')
        currentPlayer = 0

        conns = []
        while True:
            # 等待客户端连接请求,获取connSock
            conn, addr = s.accept()
            Game_Start(conn, addr)
            break
        s.close()

if __name__ == '__main__':
    main() 