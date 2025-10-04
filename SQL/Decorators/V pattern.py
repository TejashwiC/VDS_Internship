n = int(input("Enter number of rows (>=3): "))

if n < 3:
    print("Number of rows must be at least 3.")
else:
    for i in range(n):
        for j in range(2 * n - 1):
            if j == i or j == (2*n - 2 - i):
                print("*", end="")
            else:
                print(" ", end="")
        print()  
