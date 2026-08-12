class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def isEdge(r, c):
            if (r == 0 or
                c == 0 or
                r == len(board) - 1 or
                c == len(board[0]) - 1):
                return True
            return False

        invalid = []

        def dfs(r, c, visited=None):
            if visited is None:
                visited = set()

            dirs = [[0,1],[1,0],[0,-1],[-1,0]]
            invalid.append((r, c))

            for d in dirs:
                nextR = r + d[0]
                nextC = c + d[1]
                if (0 <= nextR < len(board) and
                    0 <= nextC < len(board[0]) and
                    (nextR, nextC) not in visited and 
                    board[nextR][nextC] == 'O'):
                    visited.add((nextR, nextC))
                    dfs(nextR, nextC, visited)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and isEdge(r,c) and (r, c) not in invalid:
                    dfs(r, c)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r, c) not in invalid:
                    board[r][c] = 'X'

