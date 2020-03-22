# 절댓값(abs)
num_integer=[-3, -2, -1, 0, 1, 2, 3]
num_natural= list(map(abs,num_integer))
print("a list consists of integer", num_integer)
print("can change by applying abs func to natural numbers", num_natural)

# all and any
# can check out if there is True or False type
all_true= [1, 2, 3]
any_false= [0, 2, 3, 3]
print("1. a list consists of true type elements : ", all_true)
print("2. a list including any false type elements : ", any_false)
print("by using all fuc, for the 1st >>> ", all(all_true), "\nfor the 2nd >>> ", all(any_false))
print("by using any fuc, for the 1st >>> ", any(all_true), "\nfor the 2nd >>> ", any(any_false))

# chr : convert numbers to ASKII code
# ord : convert characters to ASKII code
for i in range(97, 128):
    print(i, "in ASKII code >>> ", chr(i))

# dir func shows methods available
print("int_methods >>> ", dir(int))
print("str_methods >>> ", dir(str))
print("list_methods >>> ", dir(list))
print("tuple_methods >>> ", dir(tuple))
print("dict_methods >>> ", dir(dict))

#enumerate
for i, name in enumerate(['1st', '2nd', '3rd']):
    print(i, name)

#eval(expression)
print("eval('1+1') >>> ", eval("1+1"))
a= '123'
print(a, type(a))
print(eval(a), type(eval(a)))
f='3.14'
print('f', type(f), type(eval(f)))

# filter
def posi(x):
    return x>0
print(num_integer)
print(list(filter(posi,num_integer)))
print(list(filter(lambda x: x>0, num_integer)))

# int
# isinstance
# len
# list
# map
print(num_integer, end= " ")
print("by using map and abs func >>> ", list(map(abs, num_integer)))
print("by using lambda func >>> ", list(map(lambda x: x*x, num_integer)))

# max
# min
# pow
# range
# round(number[,ndigits])
# sorted
# str
# sum : list, set
# tuple
# type
# zip
print([1, 2, 3], [2, 4, 6])
print("by using ZIP func >>>", list(zip([1, 2, 3], [2, 4, 6])))