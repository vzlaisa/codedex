import math

print("Welcome to the calculator program!")
print("Choose a shape to calculate its area:")
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Circle")
print("5. Quit")

option = input("Enter the number corresponding to your choice: ")

area = 0
match option:
    case "1":
        side = float(input("Enter the length of the side of the square:"))
        area = side ** 2
    case "2":
        length = float(input("Enter the length of the rectangle:"))
        width = float(input("Enter the width of the rectangle:"))
        area = length * width
    case "3":
        base = float(input("Enter the base of the triangle:"))
        height = float(input("Enter the height of the triangle:"))
        area = (base * height) / 2
    case "4":
        radius = float(input("Enter the radius of the circle:"))
        area = math.pi * radius ** 2
    case "5":
        print("Goodbye!")
        exit()
    case _:
        print("Invalid option. Please try again.")
        exit()

print(f"The area is: {area}")