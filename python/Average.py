"""Average"""
def main():
    """program"""
    i = 10
    num = 0
    while i > 0 :
        i -= 1
        num += int(input())
    print(f"Average is {num/10:.2f}")
main()
