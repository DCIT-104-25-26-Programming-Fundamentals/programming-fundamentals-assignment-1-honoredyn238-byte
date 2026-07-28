# Multiplication Table
n = int(input("Enter N: "))
for i in range(1, n+1):
    print(f"\nTable of {i}:")
    for j in range(1, 13):
        print(f"{i} x {j} = {i*j}")
