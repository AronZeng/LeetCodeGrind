class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        m = len(grid)
        for i in range(m):
            for j in range(n): 
                if i == 0 and j == 0: 
                    continue
                if i - 1 < 0:
                    grid[i][j] += grid[i][j-1]
                elif j - 1 < 0: 
                    grid[i][j] += grid[i-1][j]
                else: 
                    grid[i][j] += min(grid[i-1][j] , grid[i][j-1])
        return grid[i][j]
                    
        