from source_class import Cal

class Cal_four(Cal):
    def __init__(self):
        self.result= 0
    def sub(self,a):
        self.a= a
        self.result -= self.a
        return self.result
    def div(self,b):
        self.b= b
        if self.b==0:
            return "cant be divided by 0 !!!"
        else:
            self.result /= self.b
            return self.result
    def mul(self,d):
        self.d= d
        self.result *= self.d
        return self.result

a=Cal_four()
print(a.add(5), a.sub(3), a.div(0), a.div(100), a.mul(1000)
