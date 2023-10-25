#!/usr/bin/python3

"""The Solving of the N-queens puzzle
All possible solutions related to N are determined
On NxN chessboard we have N non-attacking Queens
N must be an int greater or equal to 4
Attributes:
    board (list): list of lists representing chessboard
    solutions (list): list of lists containing solutions
The solutions are represented in [[r, c], [r, c], [r, c], [r, c]] format
where r and c representrows and columns respectively
And a queen must be placed on the chessboard
"""
import sys


def init_board(a):
    """An nxn size 0 is initialized on the chessboard
        Args:
            a: The int to initialize
        Return:
            The chessboard list
    """


board = []
for m in range(a):
    row = [' '] * a
    board.append(row)
return board


def board_deepcopy(board):
    """A deepcopy of chessboard is created
        Arg:
            board: chessboard to make copy from
        Return:
            The chessboard deepcopy
    """


if isinstance(board, list):
    return list(map(board_deepcopy, board))
return (board)


def get_solution(board):
    """List of lists representation of solved chessboard is created
        Arg:
            board: The list of chessboard
        Return:
            list of lists
    """


solution = []
for r in range(len(board)):
    for c in range(len(board)):
        if board[r][c] == "Q":
            solution.append([r, c])
            break
return (solution)


def xout(board, row, column):
    """The X out spots on a chessboard
        Spots where the non-attacking queens cannot be played
        are X-ed out
            Args:
                board (list): current working chessboard
                row (int): row where queen was last played
                column (int): column where queen was last played
    """


# All forward spots X out
for c in range(column + 1, len(board)):
    board[row][c] = "x"
# All backward spots X out
for c in range(column - 1, -1, -1):
    board[row][c] = "x"
# All spots below X out
for r in range(row + 1, len(board)):
    board[r][column] = "x"
# All spots above X out
for r in range(row - 1, -1, -1):
    board[r][column] = "x"
# All diagonal spots down to the right X out
c = column + 1
for r in range(row + 1, len(board)):
    if c >= len(board):
        break
    board[r][c] = "x"
    c += 1
# All diagonal spots up to the left X out
c = column - 1
for r in range(row - 1, -1, -1):
    if c < 0:
        break
    board[r][c]
    c -= 1
# All spots diagonal up to right X out
c = column + 1
for r in range(row - 1, -1, -1):
    if c >= len(board):
        break
    board[r][c] = "x"
    c += 1
# All spots diagonal down to the left X out
c = column - 1
for r in range(row + 1, len(board)):
    if c < 0:
        break
    board[r][c] = "x"
    c -= 1


def recursive_solve(board, row, queens, solutions):
    """Solve an N-queens puzzle recursively
        Args:
            board (list): current working chessboard
            row (int): my current working row
            queens (int): list of lists containing solutions
        Returns:
            The final solutions
    """


if queens == len(board):
    solutions.append(get_solution(board))
    return (solutions)

for c in range(len(range)):
    if board[row][c] == " ":
        temp_board = board_deepcopy(board)
        temp_board[row][c] = "Q"
        xout(temp_board, row, c)
        solutions = recursive_solve(temp_board, row + 1, queens + 1, solutions)
    return (slutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be atleast 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive.solve(board, 0, 0, [])
    for my_sol in solutions:
        print(my_sol)
