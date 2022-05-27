# encoding=gbk
import socket
import pickle
from _thread import *
from Map_Data import *

HOST = '127.0.0.1'
PORT = 5555
ADDR = (HOST, PORT)
BUFFSIZE = 1024
MAX_LISTEN = 2

Map = newMap()
    
#���յ�ͼ���ݲ��ش�
def threaded_client(conn):
    global Map
    conn.send(pickle.dumps(Map))
    while True:
        try:
            data = pickle.loads(conn.recv(2048))

            if not data:
                print("Disconnected")
                break
            else:
                #��������
                analize_map(data)
                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(Map))
        except:
            break

    print("Lost connection")
    conn.close()

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
        if bird.rect.y > FLOOR_H or bird.rect.y < 0 or pygame.sprite.spritecollideany(bird, Pipes):
            # ��������ʱ����� ���� �ܵ� ������ʾ�ڽ�������
            bird.gameover = 1
        # ��С����ߴ��� �ܵ��ұ߾͵÷�
        if Map.Pipes[0].rect.left == 0:
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

def Game_Start(currentPlay, conns):
    start_new_thread(update_pipe,())#��һ���߳�ȥȫ�ָ��µ�ͼ
    for conn in conns:
        bird = Bird(host = conn)
        Map.Birds.append(bird)
        start_new_thread(threaded_client, (conn,))
    
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
            conns.append(conn)
            print("Connected to:", addr)
            currentPlayer += 1
            if (currentPlayer == 1):
                Game_Start(currentPlayer, conns)
                break
        s.close()

if __name__ == '__main__':
    main() 