"""import math"""
import math
#I hate math!!!
def main():
    """Program"""
    x = int(input())
    y = int(input())
    n = (3*math.log(x,2) + math.cos(math.radians(x**2-y))) / math.sqrt(x+y) + math.factorial(y)
    print(format(n,".2f"))
main()
