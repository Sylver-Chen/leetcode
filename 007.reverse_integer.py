class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
        ans = 0
        x = abs(x)
        while x > 0:
            ans = ans * 10 + x % 10
            x = int(x/10)
        return sign * ans if ans <= 0x7fffffff else 0


s = Solution()
print(s.reverse(123))
