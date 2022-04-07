# function
print("select the unit")
unit = 'mm', 'cm', 'dm', 'm', 'km', 'inch', 'foot'
print(unit)
print("  1     2      3    4    5     6       7 ")
value = int(input())
value = value - 1
print("your required unit is ", (unit[value]))
print("enter the length")
length = int(input())
print("you enter", length, (unit[value]), "as a length")
print("enter the breadth")
breadth = int(input())
print("you enter", breadth, (unit[value]), "as a breadth")
print("enter the height")
height = int(input())
print("you enter", height, (unit[value]), "as a height")

# function


def area(length, breadth, height):
    return length * breadth * height


print("your resultant area is", area(length, breadth, height), unit[value], "cube")
