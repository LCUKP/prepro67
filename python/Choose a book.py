"""import math"""
import math
#Choose a book
def main() :
    """Program"""
    n = int(input())
    r = int(input())
    nCr = int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))
    print(nCr)
main()
