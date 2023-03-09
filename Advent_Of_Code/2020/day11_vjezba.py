import copy

def check_occupied(grid, node):
    if node[0] < 0 or node[0] >= len(grid) or node[1] < 0 or node[1] >= len(grid[0]):
        return True

    if grid[node[0]][node[1]] == '#':
        return False
    
    return True

def occupy_seat(grid, node):

    # grid = copy.deepcopy(grid1)

    if grid[node[0]][node[1]] == 'L':

        left = check_occupied(grid, [node[0], node[1] - 1])
        up = check_occupied(grid, [node[0] - 1, node[1]])
        right = check_occupied(grid, [node[0], node[1] + 1])
        down = check_occupied(grid, [node[0] + 1, node[1]])

        diagonal_left_up = check_occupied(grid, [node[0] - 1, node[1] - 1])
        diagonal_left_down = check_occupied(grid, [node[0] + 1, node[1] - 1])

        diagonal_right_up = check_occupied(grid, [node[0] - 1, node[1] + 1])
        diagonal_right_down = check_occupied(grid, [node[0] + 1, node[1] + 1])

        if left and up and right and down and diagonal_left_up and diagonal_left_down and diagonal_right_up and diagonal_right_down:
            grid[node[0]][node[1]] = '#'


    return grid


def change_grid(grid1):

    grid = copy.deepcopy(grid1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            occupy_seat(grid, [i,j])

    return grid


grid = [
    list('L.LL.LL.LL'),
    list('LLLLLLL.LL'),
    list('L.L.L..L..'),
    list('LLLL.LL.LL'),
    list('L.LL.LL.LL'),
    list('L.LLLLL.LL'),
    list('..L.L.....'),
    list('LLLLLLLLLL'),
    list('L.LLLLLL.L'),
    list('L.LLLLL.LL'),
]



while grid != change_grid(grid):
    grid = change_grid(grid)


print(grid)



# while grid1 != grid:
#     grid1 = change_grid(grid1)

# print(grid)
# print(grid1)
