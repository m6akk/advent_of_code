oard = []
with open("input.txt") as fp:
    lines = fp.readlines()
    for idx, line in enumerate(lines):
        arr = []
        for c in line.strip():
            arr.append(int(c))
        board.append(arr.copy())

height = len(board)
width = len(board[0])

flashed_step = []
global flashes
flashes = 0
def zero_flashed(board, fls):
    result=board.copy()
    for fl in fls:
        x, y = fl
        board[y][x] = 0

    return result


def flash(board, coord, flashed):
    grid = board.copy()
    recent_flashed = flashed.copy()
    x, y = coord
    global flashes
    flashes += 1
    grid[y][x] = 0
    flash_coords = []
    if x >= 1 and y >= 1:
        flash_coords.extend([(x-1, y-1), (x-1, y), (x, y-1)])
    if x < width -1 and y < height - 1:
        flash_coords.extend([(x+1, y+1), (x+1, y), (x, y+1)])
    if x >= 1 and y < height -1:
        flash_coords.append((x-1, y+1))
    if x < width -1 and y >= 1:
        flash_coords.append((x+1, y-1))
    if x >= 1:
        flash_coords.append((x-1, y))
    if y >= 1:
        flash_coords.append((x, y-1))
    if x < width -1:
        flash_coords.append((x+1, y))
    if y < height -1:
        flash_coords.append((x, y+1))
    
    flashing = list(set(flash_coords))# get rid of duplicates
    for co in flashing:
        grid = increment_one(grid, co)
    fcoords = scan_flash(grid)
    flashed_step.extend(fcoords)

    if len(fcoords) > 1:
        for fc in fcoords:
            if fc not in flashed_step:
                grid = flash(grid, fc, recent_flashed)
                recent_flashed.append(fc)
                flashes += 1
    return grid
            



def increment_one(board, coord):
    result = board.copy()
    x, y = coord
    if result[y][x] < 10:
        result[y][x] += 1
    return result

def increment_all(board):
    result = board.copy()
    for yid, y in enumerate(result):
        for xid, x in enumerate(y):
            result[yid][xid] += 1
    return result

def scan_flash(board):
    coords = []
    global flashes
    for yidx, y in enumerate(board):
        for xidx, x in enumerate(y):
            if x >= 10:
                coords.append((xidx, yidx))
    return coords

def print_board(board, step = 0, highlight = []):
    reset = '\033[0m'
    white = '\033[37;1m'
    cyan = '\033[36;1m'
    blue = '\033[44m'
    fgblue = '\033[34;1m'
    fgRed = '\033[31;1m'
    fgBrightRed = '\033[31;1m'

    print(u"\u001b[2J") # clear
    print(f'{blue}    0  1  2  3  4  5  6{reset} hl:{len(highlight)} fs:{len(flashed_step)}')
    for yi, y in enumerate(board):
        print(f'{blue}{yi}:{reset} ', end='')
        for xi, x in enumerate(y):
            #print(f'l:{len(y)}', end='')
            coord = (xi, yi)
            if coord in highlight:
                if x == 10:
                    print(f'{fgblue} 0 {reset}', end='')
                else:
                    print(f'{fgblue} {x} {reset}', end='')
            else:
                if x == 10:
                    print(f'{fgBrightRed} 0 {reset}', end='')
                else:
                    print(f' {x} ', end='')
        print()
    print(f'[{width}x{height} S:{step} F:{cyan}{flashes}{reset}]')

def run_model(board, steps):
    grid = board.copy()
    print_board(grid)
    input()
    for step in range(steps):
        flashed = []
        grid = increment_all(grid)
        while True:
            coords = scan_flash(grid)
            if len(coords) > 0:
                for c in coords:
                    grid = flash(grid, c, flashed)
                    flashed.append(c)
            else:
                break
        if len(flashed) == width * height: # part 2
            print_board(grid, step+ 1, flashed)
            input()
        grid = zero_flashed(grid, flashed)  
        print_board(grid, step+ 1)

run_model(board, 100) # part 1
