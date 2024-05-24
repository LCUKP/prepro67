"""Hair salon promotion"""
def main() :
    """Program"""
    time = int(input())
    if time == 0 :
        print("Not free")
    else :
        print("Free" if time%10 == 0 else "Not free")
main()
