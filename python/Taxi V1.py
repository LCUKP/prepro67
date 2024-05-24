"""Taxi V1"""
def main() :
    """Program"""
    kilo = int(input())
    price = 0
    while kilo > 0 :
        if kilo == 1 :
            price += 35
        elif kilo <= 10 :
            price += 6.5
        elif kilo <= 20 :
            price += 7
        elif kilo <= 40 :
            price += 8
        elif kilo <= 60 :
            price += 8.5
        elif kilo <= 80 :
            price += 9
        elif kilo > 80 :
            price += 10.5
        kilo = kilo - 1
    print(format(price,".2f"))
main()
