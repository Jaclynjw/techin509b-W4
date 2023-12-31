from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

# add new board
board_new = [
    "......................",
    "...######....######...",
    "...#....#....#....#...",
    "...#....#....#....#...",
    "...#....###########...",
    "...#..............#...",
    "...################...",
    "......................",
]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Implement your code here.
    def fill(x, y):
        if (
            x < 0
            or x >= len(input_board)
            or y < 0
            or y >= len(input_board[0])
            or input_board[x][y] != old
        ):
            return

        input_board[x] = input_board[x][:y] + new + input_board[x][y+1:]

        fill(x-1, y)
        fill(x+1, y)
        fill(x, y-1)
        fill(x, y+1)

    fill(x, y)
    return input_board


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# new test for new board
modified_board_new = flood_fill(input_board=board_new, old=".", new="~", x=3, y=6)

for a in modified_board_new:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....
