# If
money= True
if money:
    print("get a taxi")
else: print('walk')

print(money)

#and or
money= 2000
card= True
if money>= 3000 or card:
    print("okay to get a taxi")
else: print("better walk home")

a=range(1, 10)
print(1 in a and 10 in a)

#conditional expression
score= 59
if score >= 60:
    message= "pass"
else:
    message= "fail"
print(message)

score= 70
message = "fail" if score <60 else "pass"
print(message)

