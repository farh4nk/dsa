class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        adj_list = { i:[] for i in range(numCourses)}
        indegrees = {i:0 for i in range(numCourses)}
        for crs, pre in prerequisites:
            indegrees[crs] += 1
            adj_list[pre].append(crs)

        visited = set()
        queue = deque()
        for crs, deg in indegrees.items():
            if deg == 0:
                queue.append(crs)
        while queue:
            curr = queue.popleft()
            order.append(curr)
            visited.add(curr)
            for neighbor in adj_list[curr]:
                indegrees[neighbor] = indegrees[neighbor] - 1
                #print(indegrees)
                if indegrees[neighbor] == 0 and neighbor not in visited:
                    queue.append(neighbor)
        #print(visited, list(visited))
        return [] if len(visited) != numCourses else order