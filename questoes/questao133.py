# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, neighbors: list['Node'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        # dicionário para mapear nó original → nó clonado
        cloned = {}
        
        def dfs(n: 'Node') -> 'Node':
            # se já clonamos esse nó, retorna ele
            if n in cloned:
                return cloned[n]
            
            # cria o clone
            copy = Node(n.val)
            cloned[n] = copy
            
            # clona todos os vizinhos
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node)