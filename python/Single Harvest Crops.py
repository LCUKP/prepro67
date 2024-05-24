"""Single Harvest Crops"""
def main() :
    """Program"""
    name = input()
    time = int(input())
    price = int(input())
    amount = int(input())
    date = int(input())
    if (date + time) > 28 :
        print("The Season will end before you can harvest your "+name+"\nYour income will be 0 G")
    else :
        print("The "+name+" will be harvestable on day "+str(date + time)+" of the Season")
        print("Your income will be "+str(format(price*amount,","))+" G")
main()
