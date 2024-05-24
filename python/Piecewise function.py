"""Piecewise function"""
def main():
    """program"""
    x = float(input())
    if x <= -1 :
        x = (x**2)+1
    elif x < 2:
        x = x + 4
    elif x >= 2 :
        x = 5
    print(format(x,".2f"))
main()
