from collections import deque
from typing import List

class Solution:
    def countSubIslands(self, g1: List[List[int]], g2: List[List[int]]) -> int:
        if not g1 or not g2:
            return 0
        
        n = len(g1)
        m = len(g1[0])
        count = 0

        def bfs(i: int, j: int) -> bool:
            """
            Perform BFS to traverse the island in g2 starting at (i, j).
            Check if all corresponding cells in g1 are also land (1).
            """
            queue = deque()
            queue.append((i, j))
            g2[i][j] = 0  # Mark as visited
            is_sub_island = True

            while queue:
                x, y = queue.popleft()
                
                # If the corresponding cell in g1 is water, it's not a sub-island
                if g1[x][y] == 0:
                    is_sub_island = False

                # Explore all four directions
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy

                    # Check boundaries and if the cell is part of the island in g2
                    if 0 <= nx < n and 0 <= ny < m and g2[nx][ny] == 1:
                        queue.append((nx, ny))
                        g2[nx][ny] = 0  # Mark as visited

            return is_sub_island

        for i in range(n):
            for j in range(m):
                if g2[i][j] == 1:
                    if bfs(i, j):
                        count += 1

        return count
