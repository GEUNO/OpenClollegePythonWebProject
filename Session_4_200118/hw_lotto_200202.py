# 사용자가 입력한 1~10까지의 숫자 5개와 랜덤으로 정해지는 당첨 번호를 비교하여 당첨 갯수를 반환하는 프로그램

from random import randint

user_numbers= []
lucky_numbers= []

print("■ 1~10까지의 숫자를 5개 하나씩 입력하십니오.")

# 추첨 엔드리용 숫자를 고른다.
while 0 <= len(user_numbers) < 5:
    input_numbers= input('>')

    try:
        a= int(input_numbers)
    except:
        print('무효한 값입니다. 다시 입력하십니다.')
        continue

    if 0 > a or a > 10:
        print('1~10까지의 숫자를 입력하십시오.')
        continue
    elif a in user_numbers:
        print(user_numbers, '이외의 숫자를 입력하십시오.')
        continue
    user_numbers.append(a)

print('당신이 고른 숫자는', user_numbers, '입니다. \n')

# 당첨 번호를 고른다.
print('추첨을 시작합니다.')
while 0 <= len(lucky_numbers) < 5:
    b= randint(1,10)
    if b not in lucky_numbers:
        lucky_numbers.append(b)
    else: continue

print(lucky_numbers, '\n')

# 추첨 엔트리용 번호와 당첨 번호를 비교한다.
user_set= set(user_numbers)
lucky_set= set(lucky_numbers)
winner_set= user_set.intersection(lucky_set)
print('당첨된 숫자는', winner_set)
print('당첨된 갯수는', len(winner_set), '개 입니다.')

