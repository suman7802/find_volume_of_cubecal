while True:
    unit = 'mm', 'cm', 'dm', 'm', 'km', 'inch', 'foot'
    print(unit)
    print("  1     2      3    4    5     6       7 ")
    value = int(input("Select unit, use num "))
    value = value - 1
    print("You select ", (unit[value]))
    length = float(input("enter the length "))
    print("You enter", length, (unit[value]), "length")
    breadth = float(input("enter the breadth "))
    print("You enter", breadth, (unit[value]), "breadth")
    height = float(input("enter the height "))
    print("You enter", height, (unit[value]), "height")
    area = length * breadth * height
    print("The area is", area, unit[value], "cube")
    input1 = input("Do You Want To Calculate More? y/n ")
    if input1 == "Y" or "y":
        continue
    else:
        break
