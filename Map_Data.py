# encoding=gbk
class Map():
    class Pipe:
        def __init__(self):
            self.start = true
            self.len = 50
            self.pos = 1000
        def display(self):
            pass
    #定义鸟类
    class Bird:
        def __init__(self):
            self.name = "NewBee"
            self.dress = "Default"
            self.pos_y = 50
        def display(self):
            pass
    #定义道具
    class Prop:
        pass
    Pipes = []
    Birds = []

class Data():
    def __init__(self):
        self.index = 0
        self.up = 0
        self.prop = 0