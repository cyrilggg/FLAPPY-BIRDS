#coding: gbk
import socket               # 导入 socket 模块

def connect(host):
    Clinet_Socket = socket.socket()
    port = 65535
    Clinet_Socket.connect((host, port))
    Background_Map = Clinet_Socket.recv(1024).decode() #返回地图文件
    #返回各玩家信息文件
    #传回是否使用道具信息
    #传回多人游戏的界面
    #发送玩家操作给服务端进行更新
    Clinet_Socket.close()
