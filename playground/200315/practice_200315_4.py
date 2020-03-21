# class
result= 0
def add(num):
    global result
    result += num
    return result

print(result)
print(add(3))
print(add(4))

class Cal:
    def __init__(self):
        self.result= 0
        print(type(self))
        print(self)
        print(self.result)
    def add(self,num):
        self.result += num
        return self.result
c_1=Cal()
print(c_1.add(4))
