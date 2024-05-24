"""Marriage Guide for Farmers"""
def main() :
    """Program"""
    name = input()
    gold = int(input())
    weather = input()
    aff = int(input())
    hu = int(input())
    if weather != "rain" :
        print("*Old Mariner is missing*")
    elif aff < 10 :
        print("\"I've got this old amulet to sell... but somethin' tells me yer not ready for it, \
"+name+".\"")
    elif hu < 2 :
        print("\"I can see that sparkle in yer eye, "+name+". Ye must be head over heels in love. \
But I'm afraid a bigger house is essential for a happy marriage.\"")
    elif gold < 5000 :
        print("*Not enough money*")
    else :
        print("*You can buy the Mermaid's Pendant*")
main()
