"Johnny's cage"
def main() :
    """in function"""
    name = input()
    pos = input()
    lenname = len(name)
    print("-"*(lenname+2))
    if pos == "Left" :
        print("#"+name+"|")
    elif pos == "Right" :
        print("|"+name+"#")
    elif pos == "Both" :
        print("#"+name+"#")
    elif pos == "None" :
        print("|"+name+"|")
    print("-"*(lenname+2))
main()
