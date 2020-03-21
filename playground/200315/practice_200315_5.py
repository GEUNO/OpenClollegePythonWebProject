# Class
class Four_cal:
    def set_data(self, first, second):
        self.first= first
        self.second= second
print(Four_cal)

a= Four_cal()
a.set_data(2,3)
print(a.first)

#Constructor
class Four_cal_2:
    def __init__(self):
        passt3
    def add(self, first, second):
        self.first= first
        self.second= second
        return self.first +self.second
a_2=Four_cal_2()
result= a_2.add(3, 5)
print(result)