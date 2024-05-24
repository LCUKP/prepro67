x1 = float(input())
x2 = float(input())
t = float(input())
s = x1 - x2 if x1 > x2 else x2 - x1
print("The Velocity is",format((s/t),".2f"),"m/s")