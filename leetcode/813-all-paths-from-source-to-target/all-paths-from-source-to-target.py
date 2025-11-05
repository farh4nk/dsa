class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.graph = defaultdict(list) # map every vertex to list of vertices that can be visited
        for i, edges in enumerate(graph):
            self.graph[i] = edges

        def dfs(path, node):
            if node == len(self.graph)-1: # if you reach the end add the path
                res.append(list(path))
            else:
                for vertex in self.graph[node]:
                    path.append(vertex)
                    dfs(path, vertex)
                    path.pop()
        dfs([0], 0)
        return res