import math
str = "A"
tens = math.floor(ord(str)/10)
unit= ord(str)-(math.floor(ord(str)/10)*10)
print(tens,unit,ord(str) + abs(unit-tens)*2)
# print(math.gcd(5,14))
# print(math.floor(ord(str)/10))
# print(ord(str)-(math.floor(ord(str)/10)*10))