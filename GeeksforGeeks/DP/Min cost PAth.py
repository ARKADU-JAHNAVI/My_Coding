import heapq
class Solution:
# Function to return the minimum cost to reach bottom-right cell from top-left cell
    def minimumCostPath(self, grid):
        m = len(grid)
        n = len(grid[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        dist[0][0] = grid[0][0]
        heap = [(grid[0][0], 0, 0)]
        
        while heap:
            cost, x, y = heapq.heappop(heap)
            if cost > dist[x][y]:
                continue
            
            if x == m-1 and y == n-1:
                return cost
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost + grid[nx][ny]
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heapq.heappush(heap, (new_cost, nx, ny))
        return dist[m-1][n-1]

''' 
You can use the Dijkstra + min-heap method whenever:

You have a grid with positive costs in each cell.

You can move in all four directions (up, down, left, right).

You want the minimum total cost/path sum from a start cell to an end cell. 
'''