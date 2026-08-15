class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        rows = len(heights)
        cols = len(heights[0])

        # holds positions from which water can flow into the corresponding ocean
        pacific, atlantic = set(), set()

        def dfs(r, c, ocean):
            ocean.add((r, c))
            
            for d in dirs:
                nR = r + d[0]
                nC = c + d[1]

                # check if in bounds, not in visited, and higher cell number than current
                if (0 <= nR < rows and
                    0 <= nC < cols and
                    (nR, nC) not in ocean and
                    heights[nR][nC] >= heights[r][c]):
                    dfs(nR, nC, ocean)
            
        for i in range(cols):
            dfs(0, i, pacific)
        for j in range(rows):
            dfs(j, 0, pacific)

        for i in range(cols):
            dfs(rows-1, i, atlantic)
        for j in range(rows):
            dfs(j, cols-1, atlantic)

        res = []
        for pos in pacific:
            if pos in atlantic:
                res.append(list(pos))

        return res



            
        