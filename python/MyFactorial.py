"""MyFactorial"""
def main():
    """program"""
    num = int(input())
    n = num-1
    for i in range(n,0,-1)  :
        num = num * i
    print(num)
main()
