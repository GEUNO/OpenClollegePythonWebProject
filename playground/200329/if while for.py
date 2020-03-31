# 무한 루프
num= 0
num_next= 1
i= 0

while True:
    num= num+ num_next
    num_next = num_next +num
    i += 1
    print(num, num_next, end= " ")
    if i == 10:
        break
print("")
print("")

num= 0
num_next= 1
i= 0
while i<20:
    num= num+ num_next
    num_next = num_next +num
    i += 1
    if i<11:
        continue
    else: print(num, num_next, end= " ")
