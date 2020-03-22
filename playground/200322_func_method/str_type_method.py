# upper, lower, swapcase
a="aBc"
print(a)
print(list([a, a.upper(), a.lower(), a.swapcase()]))

# capitalize, title
char="hello python!"
print(char, "   >>>   ", list([char.capitalize(), char.title()]))

# strip
char_2= "___hello world!______"
print(char_2, "   >>>   ", char_2.strip("_"))
print(char_2, "   >>>   ", char_2.lstrip("_"))
print(char_2, "   >>>   ", char_2.rstrip("_"))

# replace
print(char_2, "   >>>   ", char_2.replace("_", "*"))
print(char_2, "   >>>   ", char_2.replace("!", " ~.~ "))

# format
print("{}, 2, 3, {}, 5")
print("{}, 2, 3, {}, 5".format('1', '4'))

# join
print("6789")
print(",".join("6789"))

# cneter, ljust, rjust
star="stars"
print(star, "\n"+star.center(20), "\n"+star.center(20,"*"))
print(star, "\n"+star.ljust(20,"*"), "\n"+star.rjust(20,"*"))

# split
a="010-1234-5678"
print(a)
print(a.split("-"))
print(a.split("-", 1))
print(a.rsplit("-", 1))

# partition
print("partition")
print(a)
print(a.partition("-"))

#splitlines

# find
a= "abcdefghijkl"
print("find".center(50,"*"))
print(a.find('a'), a.find('b'), a.find('c'), a.find('z'))
b= "abcdefgfedcba"
print(b.rfind('a'), b.rfind('b'), b.rfind('c'), b.rfind('z'))
print(b.rfind('a'), b.rfind('b'), b.rfind('c'), b.rfind('z'), sep=",")
print(b.rfind('a'), b.rfind('b'), b.rfind('c'), b.rfind('z'), sep=";")



