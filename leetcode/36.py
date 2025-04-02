# 36. Valid Sudoku
# You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false
# Note: A board does not need to be full or be solvable to be valid.
# Example 1: 
# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
# ["4",".",".","5",".",".",".",".","."],
# [".","9","8",".",".",".",".",".","3"],
# ["5",".",".",".","6",".",".",".","4"],
# [".",".",".","8",".","3",".",".","5"],
# ["7",".",".",".","2",".",".",".","6"],
# [".",".",".",".",".",".","2",".","."],
# [".",".",".","4","1","9",".",".","8"],
# [".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:
# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
# ["4",".",".","5",".",".",".",".","."],
# [".","9","1",".",".",".",".",".","3"],
# ["5",".",".",".","6",".",".",".","4"],
# [".",".",".","8",".","3",".",".","5"],
# ["7",".",".",".","2",".",".",".","6"],
# [".",".",".",".",".",".","2",".","."],
# [".",".",".","4","1","9",".",".","8"],
# [".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: There are two 1's in the top-left 3x3 sub-box.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                currNum = board[i][j]
                if currNum == ".":
                    continue
                if currNum in rows[i] or currNum in cols[j] or currNum in squares[(i // 3, j // 3)]:
                    return False
                else:
                    rows[i].add(currNum)
                    cols[j].add(currNum)
                    squares[(i // 3, j // 3)].add(currNum)
        return True


