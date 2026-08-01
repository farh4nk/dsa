class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def dfs(i, path=None):
            if path is None:
                path = []
            path.append(i)
            if i == len(graph) - 1:
                res.append(path.copy())
            else:
                for neighbor in graph[i]:
                    dfs(neighbor, path)
            path.pop()
            
        dfs(0)
        return res