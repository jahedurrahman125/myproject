from array import *
def input_to_list():
    arr = array("i", [])
    n=int(input("How many numbers do you want to process: "))
    print("Enter %d numbers:"%n)
    for i in range(n):
        j = int(input(""))
        arr.append(j)
    s = int(input("Enter the number to be searched: "))
    k = 0
    arr1 = array("i", [])
    for e in arr:
        if e == s:
            k
            arr1.append(k)
            k += 1
def main():
    input_to_list()
    if k != 0:
        print("%d shows up %d times among the numbers you have entered." % (s, k))
    else:
        print("%d is not among the numbers you have entered." % s)
main()