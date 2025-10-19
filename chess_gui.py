# chess_gui.py

def print_grid(grid):
    print("   " + "   ".join(map(str, range(8))))
    print("  " + "-" * 41)
    for i, row in enumerate(grid):
        print(i, "| " + "  ".join(f"{cell:2}" for cell in row) + " |")
    print("  " + "-" * 41)


def direction(x, y, ex, ey):
    val1, val2 = 0, 0
    if ex - x > 0: val1 = 1
    elif ex - x < 0: val1 = -1
    if ey - y > 0: val2 = 1
    elif ey - y < 0: val2 = -1
    return val1, val2


def obstraction(grid, x, y, ex, ey):
    dirx, diry = direction(x, y, ex, ey)
    stx, sty = x + dirx, y + diry
    while stx != ex or sty != ey:
        if grid[stx][sty] != '.':
            return False
        stx += dirx
        sty += diry
    return True


def straight(grid, x, y, ex, ey):
    if (x == ex or y == ey) and obstraction(grid, x, y, ex, ey):
        return True
    return False


def diagonal(grid, x, y, ex, ey):
    if abs(x - ex) == abs(y - ey) and obstraction(grid, x, y, ex, ey):
        return True
    return False


def lmove(x, y, ex, ey):
    if (abs(x - ex), abs(y - ey)) in [(2, 1), (1, 2)]:
        return True
    return False


def movable(grid, piece, x, y, ex, ey):
    color = piece[0]
    piece_type = piece[1]

    if piece_type == 'P':
        if color == 'W':
            if ex == x - 1 and ey == y and grid[ex][ey] == '.':
                return True
            if ex == x - 1 and abs(ey - y) == 1 and grid[ex][ey] != '.' and grid[ex][ey][0] != color:
                return True
        else:
            if ex == x + 1 and ey == y and grid[ex][ey] == '.':
                return True
            if ex == x + 1 and abs(ey - y) == 1 and grid[ex][ey] != '.' and grid[ex][ey][0] != color:
                return True
        return False

    elif piece_type == "Q":
        return straight(grid, x, y, ex, ey) or diagonal(grid, x, y, ex, ey)

    elif piece_type == "R":
        return straight(grid, x, y, ex, ey)

    elif piece_type == "B":
        return diagonal(grid, x, y, ex, ey)

    elif piece_type == "N":
        return lmove(x, y, ex, ey)

    elif piece_type == 'K':
        if (straight(grid, x, y, ex, ey) or diagonal(grid, x, y, ex, ey)) and abs(x - ex) <= 1 and abs(y - ey) <= 1:
            return True
        return False

    return False


def validate_move(grid, turn, x, y, ex, ey):
    piece = grid[x][y]
    if piece == '.':
        return False

    color = piece[0]
    if (turn == 0 and color == 'W') or (turn == 1 and color == 'B'):
        return False

    if movable(grid, piece, x, y, ex, ey):
        grid[ex][ey] = piece
        grid[x][y] = '.'
        return True
    return False

