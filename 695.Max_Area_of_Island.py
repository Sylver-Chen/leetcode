class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    # 以grid[i][j]为起点，寻找相连的最大岛屿，并将相邻坐标的值置0，
                    # 下次不再搜索
                    ans = max(self.dfs(grid, i, j), ans)
        return ans

    def dfs(self, grid, i, j):
        area = 0
        stack = [(i, j)]
        while stack:
            r, c = stack.pop()
            area += 1
            for r, c in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if (0 <= r < len(grid) and 0 <= c < len(grid[0])) and grid[r][c] == 1:
                    stack.append((r, c))
                    grid[r][c] = 0
        return area


s = Solution()
ans = s.maxAreaOfIsland(
    [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
)
print(ans)
