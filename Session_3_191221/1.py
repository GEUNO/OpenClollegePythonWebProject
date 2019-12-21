# List는 각가의 Element에 의미를 부여하기 어렵다.
a= list()
a.append("010-6246-1001")
a.append("010-6540-1001")

firstCalueInA= a[0]

# 대안으로 나온 dictionary
b= {"근호": "010-7178-****", "이섭": "010-1234-5678"}

GeunoValueInB= b["근호"]
print(GeunoValueInB)

phoneDictionary= {"근호":(1,2,3)}

c= dict(도한= "복정", 이섭= "대전")
print(c)

#dictionary에 존재하지 않는 key를 이용할 경우
# d= c["이근호"]   => Error 발생
# print(d)

is_heywon_exist= "혜원" in c
print(is_heywon_exist)

if is_heywon_exist:
    print(c["혜원"])
else:
    print("혜원님은 딕셔너리에 없습니다.")

c["혜원"]= "010-7890-1234"
c.pop("도한")

is_doan_exist= "도한" in c
is_heywon_exsit= "혜원" in c
print(is_heywon_exist)
print(is_doan_exist)
print("혜원" in c)

