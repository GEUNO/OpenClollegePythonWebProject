class Cal:
    def __init__(self):
        self.result= 0
        self.identify="who are u?"
    def add(self,num):
        self.num= num
        self.result += self.num
        return self.result

class Cal_default:
    def __init__(self, default):
        self.default= default
        self.result= 0
    def add_defalut(self,num):
        self.num= num
        self.default += self.num
        return self.default
    def add(self,num):
        self.num= num
        self.result += self.num
        return  self.result
