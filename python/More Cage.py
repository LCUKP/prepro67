"""import math"""
import math
#More Cage
def main() :
    """program"""
    pat1 = input()
    pat2 = input()
    pat3 = input()
    pat4 = input()
    pat5 = input()
    size = max(len(pat1),len(pat2),len(pat3),len(pat4),len(pat5))+2
    cage(pat1,size)
    cage(pat2,size)
    cage(pat3,size)
    cage(pat4,size)
    cage(pat5,size)
#Cage
def cage(name,size):
    """program"""
    front = math.floor((size-len(name))/2)
    back = math.ceil((size-len(name))/2)
    print("-"*(size+2))
    print("|"+" "*(front)+name+" "*(back)+"|")
    print("-"*(size+2))
main()
