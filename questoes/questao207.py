from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            # para fazer o curso a, precisa primeiro de b
            graph[b].append(a)
        
        UNVISITED, VISITING, VISITED = 0, 1, 2
        state = [UNVISITED] * numCourses
        
        def dfs(node: int) -> bool:
            if state[node] == VISITING:
                # encontramos um ciclo
                return False
            if state[node] == VISITED:
                # já verificado esse nó, sem ciclo vindo dele
                return True
            
            state[node] = VISITING
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            state[node] = VISITED
            return True
        
        for course in range(numCourses):
            if state[course] == UNVISITED:
                if not dfs(course):
                    return False
        
        return True
