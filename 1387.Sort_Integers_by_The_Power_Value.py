class Solution:
    def getKth(self, lo, hi, k):
        """
        type lo: int
        type hi: int
        type k: int
        rtype: int
        """
        weight_dict = {}
        for x in range(lo, hi + 1):
            x_copy = x
            weight = 0
            while x != 1:
                if x % 2 == 0:
                    x /= 2
                else:
                    x = 3 * x + 1
                weight += 1
            weight_dict[x_copy] = weight

        return sorted(weight_dict.items(), key=lambda x: (x[1], x[0]))[k - 1][0]


s = Solution()
ans = s.getKth(12, 15, 2)
print(ans)
