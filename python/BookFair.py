"""BookFair"""
def main():
    """program"""
    book = 0
    price = 1
    while book != -1:
        book = int(input())
        price = price + book
    if price >= 1500 :
        pdis = 20
    elif price >= 1000 :
        pdis = 10
    elif price >= 750 :
        pdis = 5
    else :
        pdis = 0
    if pdis :
        print(f"You got discount {pdis}%")
        print(f"Total price after discount {price-(price*pdis/100):.2f} baht.")
    else:
        print(f"Total price {price:.2f} baht.")
main()
