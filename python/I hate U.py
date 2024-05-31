"""I hate U"""
def main():
    """program"""
    text = input()
    for i in range(len(text)):
        print(i)
        if text[i] in ("u","U"):
            print(i, end="")
        else :
            print(text[i], end="")
main()
