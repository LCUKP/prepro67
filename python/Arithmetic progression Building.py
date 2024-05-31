"""Arithmetic progression Building"""
def main():
    """program"""
    opt = input()
    dr = int(input())
    start = int(input())
    loop = int(input())
    i = 0
    while i < loop:
        print(f"[ {start} ]", end='')
        if opt == "d":
            start = start+dr
        elif opt == "r":
            start = start*dr
        i += 1
main()
