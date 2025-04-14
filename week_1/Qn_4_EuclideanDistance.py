'''A program to find the Euclidean distance between two coordinates
   by taking both coordinates as input from the user'''


x1 = float(input("Enter x-coordinate of first point: "))
y1 = float(input("Enter y-coordinate of first point: "))
x2 = float(input("Enter x-coordinate of second point: "))
y2 = float(input("Enter y-coordinate of second point: "))


distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5


print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")