# 구구단
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

'''
num= int(input())
i=1

while i:
    print(num, "*", i, "=", num*i)
    i += 1
    if i>9: break
'''

num= int(input())

for i in range(1,10):
    print(num, "*", i, "=", num*i)

