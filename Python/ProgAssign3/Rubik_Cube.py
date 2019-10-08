

lis=list([])
k=1
for i in range(5):
    n=float(input("Enter the time for performance %d: "%k))
    k+=1
    lis.append(n)
lis.sort()
lis.pop(0)
lis.pop()

avg=((lis[0])+(lis[1])+(lis[2]))/3
print("The official competition score is %0.2f seconds."%avg)