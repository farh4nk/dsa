class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        seen = set()

        def dfs(r, c, i): # curr row, col, and index in word
            if i == len(word): # if word is found, true
                return True
            if (r not in range(rows) or  # if its out of bounds
                c not in range(cols) or
                word[i] != board[r][c] or # or it finds the wrong letter
                (r, c) in seen): # or we've already visited this position
                return False
            seen.add((r, c))
            res = (dfs(r+1, c, i+1) or # check all 4 directions to ssee if we can find the next letter
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            seen.remove((r, c))
            return res


        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): # if word is found, return True immediately
                    return True
        return False 