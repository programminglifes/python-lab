# printing a number triangle

x: int = int(input("Enter the number of rows: "))

for i in range(x):
    for j in range(i+1):
        p = x-i
        print(p, end=" ")
    print()
