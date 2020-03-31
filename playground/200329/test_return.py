num= 5
def say():
    global num
    return "this is \n %d" %num

a= say()
print(a)