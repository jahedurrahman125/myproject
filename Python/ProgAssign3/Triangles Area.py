from math import sqrt

def area(a,b,c):
    # calculate the sides
    s = (a + b + c) / 2
    # calculate the area
    area = sqrt((s*(s-a)*(s-b)*(s-c)))
    return area

def main():
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))
    j=area(a,b,c)
    print ("The triangle's area is %.1f"%j)

main()