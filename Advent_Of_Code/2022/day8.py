


# Define the grid as a list of lists of integers
grid = [    
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0]
]



def check_left(grid, i, j):
    max_height = grid[i][j] 

    while j > 0:
        j = j-1
        if grid[i][j] >= max_height:
            return False

    return True

def check_up():
    return

def check_right():
    return

def check_down():
    return



# for i in range (1, len(grid)-1):
#     for j in range(1, len(grid[0])-1):
#         # print(grid[i][j])
#     #    check_left 



print(check_left(grid, 1, 2))