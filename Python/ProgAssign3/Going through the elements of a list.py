from array import *
arr = array("i",[])
print("Give 5 numbers:")
for i in range(5):
    n = int(input("Next number: "))
    arr.append(n)
print("The numbers you entered that were greater than zero were:")
for j in arr:
    if j>0:

        print(j)

