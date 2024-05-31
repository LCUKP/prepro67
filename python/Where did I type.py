"""Where did I type"""
def main():
    """program"""
    text = input()
    find(text,input(),1)
    find(text,input(),2)
    find(text,input(),3)
    find(text,input(),4)
    find(text,input(),5)
#find
def find(text,strg,num):
    """program"""
    if text in strg:
        print(f"It's Here {num}")
main()
