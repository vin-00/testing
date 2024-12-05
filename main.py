import circle
import rectangle

def main():
    radius = float(input("Enter the radius of the circle: "))

    circle_area = circle.area(radius)
    circle_circumference = circle.circumference(radius)

    print("Area of the circle:",circle_area)
    print("Circumference of the circle:",circle_circumference)

    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))

    rect_area = rectangle.area(length,breadth)
    rect_perimeter = rectangle.perimeter(length,breadth)
    print("Area of the rectangle:",rect_area)
    print("Perimeter of the rectangle:",rect_perimeter)

main()
