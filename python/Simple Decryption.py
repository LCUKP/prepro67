"""Simple Decryption"""
def main():
    """program"""
    cha1 = input()
    cha2 = input()
    cha3 = input()
    cha4 = input()
    cha5 = input()
    print(cal(cha1)+cal(cha2)+cal(cha3)+cal(cha4)+cal(cha5))
#cal func
def cal(cha):
    """program"""
    num = 0
    if cha in ("a","f","k","p","u","z") :
        num = 20
    elif cha in ("b","g","l","q","v") :
        num = 21
    elif cha in ("c","h","m","r","w") :
        num = 22
    elif cha in ("d","i","n","s","x") :
        num = 23
    elif cha in ("e","j","o","t","y") :
        num = 24
    return num
main()
