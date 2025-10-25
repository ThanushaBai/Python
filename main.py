#nested loop

rows = int(input("how many rows?: "))
cols = int(input("how many columns?: "))
symbol =input("enter a symbol to use: ")

for i in range(rows):
    for j in range(cols):
        print(symbol,end=" ")
    print()