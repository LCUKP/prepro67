"""Upside-down Stair"""
def main():
    """program"""
    num = int(input())
    for i in range(num):
        print(str(" "*i)+str("*"*(num-i)))
main()
