from array import *
arr = array("i",[])
print("Give 5 numbers:")
for i in range(5):
    n = int(input("Next number: "))
    arr.append(n)
print("The numbers you entered, in reverse order:")
arr.reverse()
for j in range(5):
    print(arr[j])

