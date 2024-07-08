"""import functools"""
import functools
#Now put the pet into the Cage program function
def main() :
    """in function"""
    name = input()
    delspace = functools.reduce(lambda x, y: x+1, name, 0)
    print("-"*(12))
    print("#"+" "*(10-delspace)+name+"|")
    print("-"*(12))
main()
