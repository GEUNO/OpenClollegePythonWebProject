numbers = [1, 100, -1, 30, 5, 99, 45, 30, -2, -10]
maxi= 0
mini= 0

for i in numbers:
    x= i
    if i>maxi:
        maxi= i
    else : pass

for i in numbers:
    x= i
    if i<mini:
        mini= i
    else : pass

print(maxi)
print(mini)



#solution
max_number= numbers[0]
min_number= numbers[0]

for i in numbers:
    if i> max_number:
        max_number= i
    if i< min_number:
        min_number= i

print("최댓값은 " +str(max_number)+ "입니다.")
print("최솟값은 " +str(min_number)+ "입니다.")