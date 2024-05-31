"""Cat mess with my Keyboard"""
def main():
    """program"""
    text = input()
    result = ""
    for i in text:
        if i.isnumeric():
            i = ""
        result += i
    print(result)
main()
