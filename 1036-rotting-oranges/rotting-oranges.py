class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        mins = 0
        visited = set()
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))

        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                for d in dirs:
                    nextR = curr[0] + d[0]
                    nextC = curr[1] + d[1]
                    if (0 <= nextR < len(grid) and
                        0 <= nextC < len(grid[0]) and
                        (nextR, nextC) not in visited and
                        grid[nextR][nextC] == 1):
                        queue.append( (nextR, nextC) )
                        visited.add( (nextR, nextC) )
                        grid[nextR][nextC] = 2
            if queue:
                mins += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return mins