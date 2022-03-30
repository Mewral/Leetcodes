class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):





if __name__ == '__main__':
    s = Solution()
    b = [[0,0,0],[0,1,0],[0,0,0]]
    print(s.uniquePathsWithObstacles(b))