def count_occupied_seats(seat_layout):
    num_rows = len(seat_layout)
    num_cols = len(seat_layout[0])

    def count_adjacent_occupied_seats(row, col, seat_layout):
        num_occupied_seats = 0
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if i == row and j == col:
                    continue
                if 0 <= i < num_rows and 0 <= j < num_cols and seat_layout[i][j] == '#':
                    num_occupied_seats += 1
        return num_occupied_seats

    def apply_seating_rules(seat_layout):
        new_seat_layout = [row[:] for row in seat_layout] # make a copy of the seat layout
        for i in range(num_rows):
            for j in range(num_cols):
                if seat_layout[i][j] == 'L' and count_adjacent_occupied_seats(i, j, seat_layout) == 0:
                    new_seat_layout[i][j] = '#'
                elif seat_layout[i][j] == '#' and count_adjacent_occupied_seats(i, j, seat_layout) >= 4:
                    new_seat_layout[i][j] = 'L'
        return new_seat_layout

    while True:
        new_seat_layout = apply_seating_rules(seat_layout)
        if new_seat_layout == seat_layout: # no seats changed state
            break
        seat_layout = new_seat_layout

    num_occupied_seats = sum(row.count('#') for row in seat_layout)
    return num_occupied_seats



seat_layout = [
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

print(count_occupied_seats(seat_layout))
