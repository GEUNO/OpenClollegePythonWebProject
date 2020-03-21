#write_data_200321.py
f=open("C:\py_test\write_data_200321_2.txt",'w')
for i in range(1,11):
    if i==1:
        data= "this is the 1st line.\n"
    elif i==2:
        data= "this is the 2nd line.\n"
    elif i==3:
        data= "this is the 3rd line.\n"
    else:
        data= "this is the %dth line.\n" %i
    f.write(data)
f.close()

f=open("C:\py_test\write_data_200321_2.txt",'r')
lines= f.readlines()
for line in lines:
    print(line, end="")
f.close()


# if u open a file with command 'with ~ as'
# no need to close the file
with open("C:\py_test\write_data_200321_2.txt",'a') as f:
    data= "this is the 11th line\n"
    f.write(data)

with open("C:\py_test\write_data_200321_2.txt",'r') as f:
    lines= f.readlines()
    for line in lines:
        print(line, end="")