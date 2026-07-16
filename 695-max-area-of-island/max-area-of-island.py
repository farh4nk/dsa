class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        def helper(start: List[int]) -> int:
      # returns the area of an island from a start point [row, col]         
            dirs = [[0,1], [1,0], [0,-1], [-1,0]]
            row = start[0]
            col = start[1]
            grid[row][col] = 2
            area = 1
            for d in dirs:
                nextRow = row + d[0]
                nextCol = col + d[1]
                if (0 <= nextRow < len(grid)
                    and 0 <= nextCol < len(grid[0])
                    and grid[nextRow][nextCol] == 1):
                    grid[nextRow][nextCol] = 2
                    area += helper([nextRow, nextCol])
            return area




        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    currArea = helper([r, c])
                    maxArea = max(maxArea, currArea)
        return maxArea
