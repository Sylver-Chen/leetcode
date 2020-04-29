class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        : type tiles: str，由大写英文字母组成
        """
        # 统计词频
        counter = [0] * 26
        for s in tiles:
            counter[ord(s) - ord("A")] += 1

        def dfs(counter):
            res = 0
            # 给定词频，返回所有可能的结果数目
            for i in range(26):
                if counter[i] == 0:
                    continue
                else:
                    res += 1
                    counter[i] -= 1
                    res += dfs(counter)
                    counter[i] += 1
            return res

        res = dfs(counter)
        return res


s = Solution()
ans = s.numTilePossibilities("AAABBC")
print(ans)
