# 홍길동 씨의 과목별 점수의 평균을 구해보자.
scores= {'국어':80, '영어':75, '수학':55}
total= 0
subjects= list(scores.keys())
for i in subjects:
    total += scores[i]

avg= total/(len(subjects))
print(avg)


# 자연수 13이 홀수인지 짝수인지 판별하는 방법
num= 13
if num%2==0:
    print("it is odd")
else: print("it is even")

#slicing test
pin= "881120-1068234"
yyyymmdd= "19"+pin[:6]
num= pin[-7:]
print(yyyymmdd, num)

#주민등록번호에서 남녀 판별
if int(num[0])==1:
    print("male")
else: print('female')

#replace function
a='a:b:c:d'
b=a.replace(":",'#')
print((b))

#list_reverse
a_1=[1, 3, 5, 4,2]
b_2=sorted(a_1,reverse=True)
print(a_1,">>>", b_2)

# transform a list to a sting
aa= ['life','is','too','short']
bb= " ".join(aa)
print(aa, ">>>", bb)