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

#���µ�ͼ
def analize_map(Data):
    global Map
    if Data.Gameover:
        return
    #ʹ�õ���
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
            # ��������ʱ����� ���� �ܵ� ������ʾ�ڽ�������
            bird.gameover = 1
        
        #��С����ߴ��� �ܵ��ұ߾͵÷�
        if min(Map.Pipes[0].trect.x, Map.Pipes[1].trect.x) < bird.rect.x:
            bird.score += 1
     
    #��ײ�˾�ɾ��
    
#���÷�����

#�̣߳�һֱ��������
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
    start_new_thread(update_pipe,())#��һ���߳�ȥȫ�ָ��µ�ͼ
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
                #��������
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
        # �󶨷�������ַ�Ͷ˿�
        s.bind(ADDR)
        # �����������
        s.listen(MAX_LISTEN)
        print('Wating')
        currentPlayer = 0

        conns = []
        while True:
            # �ȴ��ͻ�����������,��ȡconnSock
            conn, addr = s.accept()
            Game_Start(conn, addr)
            break
        s.close()

if __name__ == '__main__':
    main() 