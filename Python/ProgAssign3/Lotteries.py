import math
from fractions import Fraction

def fact ():
    n=int(input("Enter the total number of lottery balls: "))
    p=int(input("Enter the number of the drawn balls: "))
    if n < 0 or p < 0:
        print("The number of balls must be a positive number.")
    elif n>0 and p>0:
        A=abs(math.factorial(n))
        B=abs(math.factorial(p))
        C=math.factorial(n-p)
        value = int(A / (C * B))
        out=print("The probability of guessing all %d balls correctly is 1/%d" % (p, value))
        return out
def main():
    fact()
main()