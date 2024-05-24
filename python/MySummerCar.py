"""MySummerCar"""
def main():
    """Program"""
    fuel = float(input())
    distance = float(input())
    if fuel > 5 :
        print("Impossible!!!")
    elif fuel * 5 >= distance :
        print("You have enough fuel to get to Teimo's shop.")
    elif fuel * 5 < distance :
        print("You do not have enough fuel to get to Teimo's shop.")
main()
