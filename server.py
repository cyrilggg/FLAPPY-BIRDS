# encoding=gbk
import socket
import pickle
from _thread import *
import Map_Data import Map, Data

HOST = '192.168.1.37'
PORT = 5555
ADDR = (HOST, PORT)
BUFFSIZE = 1024
MAX_LISTEN = 2

Map = Map()
start_time = time.time()

#接收地图数据并回传
def threaded_client(conn):
    conn.send(pickle.dumps(Map))
    while True:
        try:
            data = pickle.loads(conn.recv(2048))

            if not data:
                print("Disconnected")
                break
            else:
                #更新数据
                analize_map(data)
                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(Map))
        except:
            break

    print("Lost connection")
    conn.close()

#更新地图
def analize_map(Data):
    global Map
    if Map.Data.Gameover:
        return
    if Map.Data.up:
        Map.Birds[Map.Data.index] += 5
    #使用道具
    if Map.Data.Prop:
        pass

    #碰撞了就删掉
    for Bird in Map.Birds:
        if (pygame.sprite.spritecollide(Bird, Map.Pipes, True)):
            pass
#设置服务器

#线程：一直更新柱子
def update_pipe():
    global Map
    while True:
        newPipe = []
        if len(Map.Birds) == 0:
            return
        for Pipe in Map.Pipes:
            Pipe.pos -= 5
            if Pipe.pos >= 0:
                newPipe.append(Pipe)
        if newPipe[-1].pos < 95:
            APipe = Map.Pipe()
            newPipe.append(APipe)
        
        Map.Pipes = newPipe

def init():
    global HOST, PORT, ADDR
    HOST = '192.168.1.37'
    PORT = 5555
    ADDR = (HOST, PORT)

def Game_Start(conns):
    start_new_thread(update_pipe)#开一个线程去全局更新地图
    for conn in conns:
        start_new_thread(threaded_client, (conn))
    
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
            conns.append(conn)
            print("Connected to:", addr)
            currentPlayer += 1
            if (True == 5):
                Game_Start(currentPlayer, conns)
                break
        s.close()

if __name__ == '__main__':
    main() 