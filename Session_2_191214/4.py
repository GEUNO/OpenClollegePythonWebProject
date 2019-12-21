# LIST의 생성은 list() 나 []를 사용한다. (동치)

a= list()
print(type(a))

b= []
print(type(b))

c= [1, 2, 3]
d= ["chicken", "pizza", "galbi"]
print(c)
print(type(c))
print(d)

print(c[0])
print(type(c[0]))
print(c[1])
print(c[2])

print(len(c))

c[1]= -1
print(c)

