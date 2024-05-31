"""Electrical Bill"""
def main():
    """program"""
    a = int(input())
    tv_unit = unit(a,3)*30
    b = int(input())
    mircrowave_unit = unit(b,1)*30
    c = int(input())
    hairdryer_unit = unit(c,0.5)*30
    d = int(input())
    lightbulb_unit = (unit(d,5)*4)*30
    e = int(input())
    refrigerator_unit = unit(e,24)*30
    print(f"TV {a} Watt 1 ea for 3 hours\n{tv_unit:.2f} unit.")
    print(f"Microwave {b} Watt 1 ea for 1 hours\n{mircrowave_unit:.2f} unit.")
    print(f"Hair dryer {c} Watt 1 ea for 0.5 hours\n{hairdryer_unit:.2f} unit.")
    print(f"Light bulb {d} Watt 4 ea for 5 hours\n{lightbulb_unit:.2f} unit.")
    print(f"Refrigerator {e} Watt 1 ea for 24 hours\n{refrigerator_unit:.2f} unit.")
#Unit cal
def unit(watt,hour):
    """program"""
    u = (watt*hour)/1000
    return u
main()
