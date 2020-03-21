# While
tree_hit=0
while tree_hit<5:
    tree_hit +=1
    print("%d번 나무를 찍었습니다." % tree_hit)
if tree_hit==5:
    print("나무 넘어갑니다.")
else: pass

prompt='''
    1. Add
    2. Del
    3. List
    4. Quit
    
    Enter number'''
print(prompt)
num= int(input())
while num!=4:
    print(prompt)
    num= int(input())
if num==4:
    print("BYE!")

# COFFE Machine
coffee= 3
while coffee !=0:
    money= int(input('insert money:'))
    if money== 300:
        coffee -= 1
        print("wait for a sec!")
    elif money >300:
        coffee -= 1
        exchnage= money-300
        print("here the echange: %d" % exchnage)
    else:
        print("not enough money")
        print("%d coffee available" % coffee)
print("no more available")