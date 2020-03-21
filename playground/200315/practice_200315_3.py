# many inputs
def add_many(*args):
    result= 0
    for i in args:
        result += i
    return result
result= add_many(1, 2, 3)
print(result)

# many inputs and the result class dict
def print_kwargs(**kwargs):
    print(kwargs)
    return kwargs
result= print_kwargs(a=1)
print(result)

# another use of return
def say_nick(nick):
    if nick== "dumb":
        return
    else: pass
    print("my nickname is %s" % nick)

result_1= say_nick("dumb")
print(result_1)   #no retuen value
result_2= say_nick("genious")
print(result_2) # no return value


# lambda
add= lambda a, b:a+b
result= add(2,3)
print(result)
