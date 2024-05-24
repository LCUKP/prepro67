"""Days from today"""
def main():
    """Program"""
    n = int(input())
    index = n%7
    day = ""
    if index == 0 :
        day = "Tuesday"
    elif index == 1 :
        day = "Wednesday"
    elif index == 2 :
        day = "Thursday"
    elif index == 3 :
        day = "Friday"
    elif index == 4 :
        day = "Saturday"
    elif index == 5 :
        day = "Sunday"
    elif index == 6 :
        day = "Monday"
    print(format(n,","),"days from today will be",day+"!")
main()
