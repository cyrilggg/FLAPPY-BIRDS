#coding: gbk
import socket               # ���� socket ģ��

def connect(host):
    Clinet_Socket = socket.socket()
    port = 65535
    Clinet_Socket.connect((host, port))
    Background_Map = Clinet_Socket.recv(1024).decode() #���ص�ͼ�ļ�
    #���ظ������Ϣ�ļ�
    #�����Ƿ�ʹ�õ�����Ϣ
    #���ض�����Ϸ�Ľ���
    #������Ҳ���������˽��и���
    Clinet_Socket.close()
