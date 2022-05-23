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

#���յ�ͼ���ݲ��ش�
def threaded_client(conn):
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
    if Map.Data.Gameover:
        return
    if Map.Data.up:
        Map.Birds[Map.Data.index] += 5
    #ʹ�õ���
    if Map.Data.Prop:
        pass

    #��ײ�˾�ɾ��
    for Bird in Map.Birds:
        if (pygame.sprite.spritecollide(Bird, Map.Pipes, True)):
            pass
#���÷�����

#�̣߳�һֱ��������
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
    start_new_thread(update_pipe)#��һ���߳�ȥȫ�ָ��µ�ͼ
    for conn in conns:
        start_new_thread(threaded_client, (conn))
    
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
            if (True == 5):
                Game_Start(currentPlayer, conns)
                break
        s.close()

if __name__ == '__main__':
    main() 