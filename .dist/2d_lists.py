number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[0][1])#will print 2
#to access all elements in the list
for row in number_grid:
    for col in row:
        print(col)
