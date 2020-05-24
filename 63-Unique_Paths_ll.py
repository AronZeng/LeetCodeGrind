class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])
        memo = [[0 for i in range(columns)] for j in range(rows)]
        for i in range(rows): 
            for j in range(columns):
                if obstacleGrid[i][j] == 1: 
                    memo[i][j] = 0
                elif i == 0 and j == 0:
                    memo[0][0] = 1
                elif i - 1 < 0: 
                    memo[i][j] += memo[i][j-1]
                elif j - 1 < 0: 
                    memo[i][j] += memo[i-1][j]
                else: 
                    memo[i][j] += memo[i-1][j] + memo[i][j-1]
        return memo[rows - 1][columns -1]