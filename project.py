import math
def adjacent_cos(theta, hypotenuse):
    adjacent=0
    adjacent==math.cos(theta)*hypotenuse
    return adjacent
def opposite_sin(theta, hypotenuse):
    opposite=0
    opposite==math.sin(theta)*hypotenuse
    return opposite
def hypotenuse_sin(theta, opposite):
    hypotenuse=0
    hypotenuse==opposite/math.sin(theta)

print("Are you trying to find the adjacent, the hypotenuse or opposite?   ")
what_calc=input("Which?   ")
if what_calc.lower=="adjacent":
    theta=int(input("Enter the angle (theta): "))
    hypotenuse=int(input("Enter hypotenuse: "))
    print("The adjacent is:", adjacent_cos(theta, hypotenuse))
if what_calc.lower=="opposite":
    theta=int(input("Enter the angle (theta): "))
    hypotenuse=int(input("Enter hypotenuse: "))
    print("The opposite is:", opposite_sin(theta, hypotenuse))
if what_calc.lower=="hypotenuse":
    theta=int(input("Enter the angle (theta): "))
    opposite=int(input("Enter opposite: "))
    print("The adjacent is:", hypotenuse_sin(theta, opposite))

    
    
