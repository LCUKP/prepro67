"""import math"""
import math
#Caesar shift
def main():
    """Program"""
    chr1 = input()
    chr2 = input()
    chr3 = input()
    chr4 = input()
    pos = input()
    print(f"{shift(chr4,pos)}-{shift(chr3,pos)}-{shift(chr2,pos)}-{shift(chr1,pos)}")
#shift
def shift(strg,pos):
    """Program"""
    tens = math.floor(ord(strg)/10)
    unit= ord(strg)-(math.floor(ord(strg)/10)*10)
    if pos == "RIGHT":
        shr = ord(strg) + abs(unit-tens)*2
        if shr > 90 :
            shr = shr - 26
    elif pos == "LEFT" :
        shr = ord(strg) - abs(unit-tens)*2
        if shr < 65 :
            shr = shr + 26
    return chr(shr)
main()
