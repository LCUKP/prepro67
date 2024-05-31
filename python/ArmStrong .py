"""ArmStrong"""
def main():
    """program"""
    num = str(input())
    ArmStrong = 0
    for i in num:
        ArmStrong = ArmStrong + (int(i) ** len(num))
    if ArmStrong == int(num):
        print(num+" is a ArmStrong number")
    else:
        print(num+" is not a ArmStrong number")
main()
