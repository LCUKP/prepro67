"""British accent"""
def main():
    """program"""
    text = input()
    print(text[:1],end="")
    for i in range(1,len(text)-1):
        if text[i] != "t":
            print(text[i],end="")
    print(text[len(text)-1:],end="")
main()
