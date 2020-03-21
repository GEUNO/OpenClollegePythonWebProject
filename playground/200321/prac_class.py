# calculator w/o class

result=0
def add(num):
    global result
    result += num
    return  result
result=add(2)
print("default(0) + 2 equal",end=" ")
print(result)
result=add(3)
print("2+3 equal", end=" ")
print(result)

class Cal:
    def __init__(self):
        self.result= 0
        self.identify="who are u?"
    def add(self,num):
        self.num= num
        self.result += self.num
        return self.result

#basic calulator

# with open("C:\py_test\\basic_cal.py",'w') as f:
#    f.write('''
a=Cal()
print(a.result)
print(a.identify)
print(type(a.identify))
print("default(0) + 3 equal", a.add(3))
print("3 + 100 equal", a.add(100))

b=Cal()
print("default(0) + 5 equal", b.add(5))
print("default(0) + 100 equal", b.add(100))

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

c=Cal_default(-1)
print(c.add_defalut(100), "is 99")
print(c.add(1000), "is 1000")
#''')
