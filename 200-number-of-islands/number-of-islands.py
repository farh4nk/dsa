class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        seen = set()
        rows, cols = len(grid), len(grid[0])
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]

        def bfs(rw, cl):
            q = deque() # queue to keep track of current island
            q.append((rw, cl)) # add curr pos to seen and curr island
            #seen.add((rw, cl))
            while q:
                currRow, currCol = q.popleft() # get current pos via popleft
                for dr, dc in dirs:
                    newRow = currRow + dr # explore all directions from curr pos
                    newCol = currCol + dc

                    if (newRow in range(rows) and # if its in range
                        newCol in range(cols) and
                        grid[newRow][newCol] == '1' and # and its land
                        (newRow, newCol) not in seen # and we haven't already seen it
                    ):
                        q.append((newRow, newCol)) # add new pos to the curr island
                        seen.add((newRow, newCol)) # and add it to seen positions

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in seen: # if we come across land we haven't seen
                    bfs(r, c) # do bfs to look for rest of island
                    islands += 1 # found new island, increment
        return islands