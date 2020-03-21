# ASKII code

with open("C:\py_test\ASKII_code.txt",'w') as f:
    for i in range(0, 128):
        data=str(i) + "   >>>   " + str(chr(i))+ "   in ASKII code" + "\n"
        f.write(data)

with open("C:\py_test\ASKII_code.txt",'r') as f:
    lines= f.readlines()
    for line in lines:
        print(line,"")


for i in range(0, 128):
    print(chr(i), end= " ")
