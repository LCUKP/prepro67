"""import math"""
import math
#Sour Soup Restaurant
def main():
    """program"""
    gang = ""
    dis = 0
    price = 0
    while gang != "stop":
        gang = input()
        if gang == "shrimp sour soup":
            price += 80
        elif gang == "mixed vegetables sour soup":
            price += 60
        elif gang == "papaya sour soup":
            price += 55
        elif gang == "snapper fish sour soup":
            price += 100
        elif gang == "cha om shrimp sour soup":
            price += 100
    if price >= 200:
        dis = int(math.floor(price*15/100))
        total = price-dis
    else :
        total = price
    print(f"Original Price {price} baht")
    print(f"Discount {dis} baht")
    print(f"Total {total} baht")
main()
