class DSU:
    def __init__(self, N):
        self.parents = [-1 for i in range(N)]

    def find(self, i):
        if self.parents[i] == -1:
            return i
        else:
            return self.find(self.parents[i])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            self.parents[xroot] = yroot

    def count(self):
        count = 0
        for x in self.parents:
            if x == -1:
                count += 1
        return count


class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype int
        """
        N = len(grid)
        dsu = DSU(N * N * 4)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r * N + c)
                if val in "/ ":
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 2, root + 3)
                if val in "\ ":
                    dsu.union(root + 0, root + 2)
                    dsu.union(root + 1, root + 3)
                if r + 1 < N:
                    dsu.union(root + 3, root + 4 * N + 0)
                if r - 1 >= 0:
                    dsu.union(root + 0, root - 4 * N + 3)
                if c + 1 < N:
                    dsu.union(root + 2, root + 4 * 1 + 1)
                if c - 1 >= 0:
                    dsu.union(root + 1, root - 4 * 1 + 2)
        return dsu.count()


s = Solution()
# ans = s.regionsBySlashes([" /", "/ "]) # 2
# ans = s.regionsBySlashes([" /", "  "])  # 1
# ans = s.regionsBySlashes(["\\/", "/\\"])  # 4
ans = s.regionsBySlashes(["/\\", "\\/"])  # 5
print(ans)
