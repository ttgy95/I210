#change name of input
rows = eval(input("How many rows should we have?"))
cols = eval(input("How many columns should we have?"))
#rows to i
for i in range(rows):
    print("Row", i, ":", end = '')
    #end=" ", empty space.
    for j in range(cols):
        print(j, end=" ")

    print()
