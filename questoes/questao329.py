class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        # dp[i][j] = comprimento da longest increasing path começando em (i, j)
        dp = [[0] * n for _ in range(m)]
        
        # 4 direções: cima, baixo, esquerda, direita
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(i: int, j: int) -> int:
            # se já calculei dp para essa célula, retorna
            if dp[i][j] != 0:
                return dp[i][j]
            
            max_len = 1  # ao menos a própria célula
            
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                # checa fronteiras e se é estritamente crescente
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    length = 1 + dfs(ni, nj)
                    if length > max_len:
                        max_len = length
            
            dp[i][j] = max_len
            return dp[i][j]
        
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        
        return result