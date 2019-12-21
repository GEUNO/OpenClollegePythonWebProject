menu= {'라면': 4000, '만두': 3500, '보쌈': 28000}

food= input("메뉴를 입력하세요 :")

if food in menu:
    cost= menu[food]
    print(food+"은 "+ str(menu[food])+"원 입니다.")
else:
    print(food+ "란 메뉴는 없습니다.")
