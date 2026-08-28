class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        visited = set()
        
        # find the rest of an island when new land is discovered
        def find(r, c):
            visited.add((r, c))

            for d in dirs:
                nR = r + d[0]
                nC = c + d[1]

                if ((nR, nC) not in visited and
                    0 <= nR < len(grid) and
                    0 <= nC < len(grid[0]) and
                    grid[nR][nC] == '1'):
                    find(nR, nC)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visited:
                    islands += 1
                    find(row, col)

        return islands
