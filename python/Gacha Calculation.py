import math
"""Gacha Calculation"""
def main():
    """Calculation"""
    pyroxene = int(input())
    count = math.floor(pyroxene/120)
    remain = (pyroxene%120)
    print("You can pull",count,"times.\nYou have",remain,"Pyroxene left.")
main()