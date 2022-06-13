from typing import List
import collections


def isValidSudoku(board: List[List[str]]) -> bool:
    n = 9
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    grid = collections.defaultdict(set)

    for x in range(n):
        for y in range(n):
            val = board[x][y]

            if val == '.':
                continue

            # check the row
            if val in rows[x]:
                return False
            else:
                rows[x].add(val)

            # check column
            if val in cols[y]:
                return False
            else:
                cols[y].add(val)

            # check the grid
            if val in grid[(x // 3, y // 3)]:
                return False
            else:
                grid[(x // 3, y // 3)].add(val)

    return True


if __name__ == "__main__":
    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    result = isValidSudoku(board)
    print(f'Result should be False: {result}')

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    result = isValidSudoku(board)
    print(f'Result should be True: {result}')
