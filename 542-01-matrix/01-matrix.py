from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return []
        
        n, m = len(mat), len(mat[0])
        dist = [[float('inf')] * m for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # BFS from all '0' cells
        while q:
            i, j = q.popleft()
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                
                # If the neighboring cell is within bounds and can be updated with a smaller distance
                if 0 <= ni < n and 0 <= nj < m and dist[ni][nj] > dist[i][j] + 1:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
        
        return dist
