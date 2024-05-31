"""MultiplicationTable"""
def main():
    """program"""
    num = int(input())
    for i in range(1,13) :
        print(f"{num} x {i} = %d"%(num*i))
main()
