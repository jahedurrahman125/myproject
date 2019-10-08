
time=[630, 1015, 1415, 1620, 1720, 2000]

n = int(input("Enter the time (as an integer): "))
k=0
print("The next buses leave:")
for i in range(6):
    if time[i]>=n:
        k
    else:
        k+=1
for j in range(3):
    if k==6:
        k=0
        print(time[k])
        k+=1
    elif k==7:
        K=1
        print(time[k])
        k += 1
    else:
        print(time[k])
        k += 1