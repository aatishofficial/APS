# leetcode - https://leetcode.com/problems/course-schedule
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        for x,y in prerequisites:
            graph[y].append(x)
        visited=[0]*numCourses
        onstack=[0]*numCourses
        for i in range(numCourses):
            if self.dfs(graph,i,visited,onstack):
                return False
        return True
    
    def dfs(self,graph,v,visited,onstack):
        if visited[v]==0:
            visited[v]=1
            onstack[v]=1
            for x in graph[v]:
                if visited[x]==0 and self.dfs(graph,x,visited,onstack):
                    return True
                elif onstack[x]==1:
                    return True
        onstack[v]=False
        return False
