#coding: gbk
import socket
import pickle
from Map_Data import *

class Network:
    def __init__(self, ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ip
        self.port = 5555
        self.addr = (self.server, self.port)
 
    def connect(self):
        self.client.connect(self.addr)  

    def send(self, data):
        try:
            self.client.sendall(pickle.dumps(data))
            #print("发送成功")
            return pickle.loads(self.client.recv(2048))
        except Exception as e:
            import traceback
            traceback.print_exc()
    
    def send_msg_to_server(self, msg):
        self.client.sendall(msg.encode())

    def recieve_msg(self):
        data = self.client.recv(1024)
        return data.decode()

    def close_connection(self):
        self.client.close()