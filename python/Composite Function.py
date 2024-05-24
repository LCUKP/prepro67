"""Composite Function"""
def main():
    """program"""
    x = float(input())
    y = float(input())
    print(format(h(x,y),".2f"))
#Piecewise function
def f(x):
    """program"""
    num = 3*x+5
    return num
#function
def g(x):
    """program"""
    num = (f(4*x) + 23)/2
    return num
#function
def h(x,y):
    """program"""
    cal = (g(f(3*y)+2*x) - g(2*y))*(f(4*y)+5*x)
    return cal
main()
