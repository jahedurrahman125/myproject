from math import sqrt
x=""
while x!=("s","r","q"):
    x=str(input("Enter the pattern's first letter, q stops this (s/r/q): "))
    if x=="s":
        A=float(input("Enter the length of the square's side: "))
        square= float(4*A)
        surf=sqrt(A)
        print("The total circumference is %f" %square)
        print("The surface area is %f" %surf)
        print("")
    elif x=="r":
        C= float(input("Enter the length of the square's side: "))
        D = float(input("Enter the length of the square's side: "))
        rect = float((2*C)+(2*D))
        surfs= float(C*D)
        print("The total circumference is %f" % rect)
        print("The surface area is %f" %surfs)
        print("")
    elif x == "c":
        rad = float(input("Enter the circle's radius: "))
        rec = float(2*rad*3.14)
        surff = float(3.14*(sqrt(rad)))
        print("The total circumference is %f" % rec)
        print("The surface area is %f" % surff)
        print("")
    elif x=="q":
        print("Goodbye!")
    else:
        print("Incorrect entry, try again!")

