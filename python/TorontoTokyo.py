"""TorontoTokyo"""
def main():
    """Program"""
    reg = input()
    hour = int(input())
    minu = int(input())
    chour = 0
    if reg == "Toronto" :
        while chour != 13:
            chour += 1
            hour += 1
            if hour == 24 :
                hour = 0
        hour = str(hour)
        minu = str(minu)
        if len(hour) == 1 :
            hour = "0"+hour
        if len(minu) == 1 :
            minu = "0"+minu
        print(f"Now in Tokyo, it's {hour}:{minu}")
    elif reg == "Tokyo" :
        if not hour :
            hour = 24
        while chour != 13:
            chour += 1
            hour -= 1
            if not hour :
                hour = 24
        hour = "00" if hour == 24 else hour
        hour = str(hour)
        minu = str(minu)
        if len(str(hour)) == 1 :
            hour = "0"+str(hour)
        if len(str(minu)) == 1 :
            hour = "0"+str(minu)
        print(f"Now in Toronto, it's {hour}:{minu}")
    else :
        print("Error, Not Toronto or Tokyo.")
main()
