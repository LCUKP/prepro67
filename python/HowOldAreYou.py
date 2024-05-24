"""HowOldAreYou"""
def main():
    """Program"""
    bornd = int(input())
    bornm = int(input())
    borny = int(input())
    date = int(input())
    month = int(input())
    years = int(input())
    if borny <= years :
        if bornm > month and borny == years :
            print((years-borny)-1)
        elif bornm == month :
            if bornd > date :
                if month == bornm and years == borny :
                    print("Error")
                else :
                    print((years-borny)-1)
            else :
                print(years-borny)
        elif bornm < month :
            print(years-borny)
    else :
        print("Error")
main()
