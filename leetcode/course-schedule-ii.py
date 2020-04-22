# leetcode - https://leetcode.com/problems/course-schedule-ii/
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        for x,y in prerequisites:
            graph[y].append(x)
        visited=[0]*numCourses
        onstack=[0]*numCourses
        stack=[]
        for i in range(numCourses):
            if visited[i]==0 and  self.dfs(graph,i,visited,onstack,stack):
                return []
        return stack[::-1]
                
    def dfs(self,graph,v,visited,onstack,stack):
        if visited[v]==0:
            visited[v]=1
            onstack[v]=1
            for x in graph[v]:
                if visited[x]==0 and self.dfs(graph,x,visited,onstack,stack):
                    return True
                elif onstack[x]==1:
                    return True
        onstack[v]=False
        stack.append(v)
        return False
