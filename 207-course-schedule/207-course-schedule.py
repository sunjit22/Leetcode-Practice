from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        hashmap = defaultdict(list)

        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            hashmap[prevCourse].append(nextCourse)
        
#         visited = {}
#         arr = []
#         for course in range(numCourses):
#             if course in visited:
#                 return False
#             elif course not in visited:
#                 res = self.dfs(course, visited, hashmap ,arr)
                
#         return True
        

#     def dfs(self,course, visited, hashmap, arr):
#         visited[course] = True
#         for c in hashmap[course]:
#             if c not in visited:
#                 self.dfs(c,visited, hashmap,arr)

#         arr.append(course)   

        path = [False]*numCourses
        for course in range(numCourses):
            if self.is_cyclic(course, hashmap, path):
                return False
        return True
    
    
    def is_cyclic(self, course, hashmap, path):        
        if path[course] == "CHECKING":
            return True
        
        if path[course] == "COMPLETED":
            return False
        
        path[course] = "CHECKING"
        for child in hashmap[course]:
            if self.is_cyclic(child, hashmap, path):
                return True
                
        path[course] = "COMPLETED"
        return False