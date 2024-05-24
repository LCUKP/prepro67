"""This Game Size Is Too Big!"""
def main() :
    """Program"""
    gamesize = float(input())
    space = float(input())
    print("This game size is "+str(format((gamesize/space*100),".2f"))+"% of your directory size")
main()
