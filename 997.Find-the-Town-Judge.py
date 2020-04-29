class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N == 1:
            return 1
        in_d, out_d = [0] * N, [0] * N
        for a, b in trust:
            out_d[a - 1] += 1
            in_d[b - 1] += 1
        # 出度为0，入度为N-1的节点即为法官
        for i in range(N):
            if out_d[i] == 0 and in_d[i] == N - 1:
                return i + 1
        return -1


s = Solution()
ans = s.findJudge(3, [[1, 3], [2, 3]])
print(ans)
