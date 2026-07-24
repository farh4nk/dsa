class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build the adjacency list
       adj_list = {i:[] for i in range(numCourses)}
       for c, p in prerequisites:
           adj_list[c].append(p)


       visited = set()


       # helper function to see if there is a path from a node to the end of the graph
       def helper(course):
           if course in visited:
               return False
           if adj_list[course] == []:
               return True
           visited.add(course)


           for p in adj_list[course]:
               if not helper(p):
                   return False
           visited.remove(course)
           adj_list[course] = []
           return True
      
       for crs in adj_list:
           if not helper(crs):
               return False
       return True
